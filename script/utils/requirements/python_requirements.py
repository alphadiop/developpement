
import subprocess
from typing import List, Tuple

import pandas as pd
import pkg_resources

from logger import LOGGER
from requirements.compare_version import compare_version
from requirements.print_logger import print_logger


def all_python_distribution(system_requirements: pd.DataFrame, logger: LOGGER) -> None:
    checks = [conda_distribution(system_requirements), python_distribution(system_requirements)]
    print_logger('Python', 'Distribution', checks, logger)


def conda_distribution(system_requirements: pd.DataFrame) -> Tuple[str, str, str, str]:
    version_require = (system_requirements[(system_requirements.Language == 'conda') & (system_requirements.Library == 'distribution')]['Requirement']
                       .values.tolist()[0])

    version_actuel = (subprocess.Popen(['conda-build', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       encoding='utf-8')
                      .communicate()[0].split('\n')[0].split(' ')[1])

    return 'conda', version_require, version_actuel, 'OK' if compare_version(version_actuel, version_require) else 'NOOK'


def python_distribution(system_requirements: pd.DataFrame) -> Tuple[str, str, str, str]:
    version_require = (system_requirements[(system_requirements.Language == 'python') & (system_requirements.Library == 'distribution')]['Requirement']
                       .values.tolist()[0])

    version_actuel = (subprocess.Popen(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                      .communicate()[0].decode('utf-8').rstrip().split(' ')[1])

    return 'python', version_require, version_actuel, 'OK' if compare_version(version_actuel, version_require) else 'NOOK'


def get_python_libraries() -> pd.DataFrame:
    library, version = list(), list()
    for i in pkg_resources.working_set:
        library.append(i.key)
        version.append(i.version)
    return pd.DataFrame({'Version': version}, index=library)


def python_libraries(system_requirements: pd.DataFrame) -> List[Tuple[str, str, str, str]]:
    python_libraries = get_python_libraries()

    libraries_version = system_requirements[(system_requirements.Language == 'python') & (system_requirements.Library != 'distribution')][['Library', 'Requirement']]
    libraries_version.set_index('Library', inplace=True)

    checks = list()
    for row in libraries_version.itertuples():
        version_requis = libraries_version.loc[row.Index].Requirement
        if row.Index in python_libraries.index:
            version_actuel = python_libraries.loc[row.Index].Version
            checks.append((row.Index, version_requis, version_actuel,
                           'OK' if compare_version(version_actuel, version_requis) else 'NOOK'))
        else:
            checks.append((row.Index, version_requis, '?', 'NOOK'))
    return checks


def all_python_libraries(system_requirements: pd.DataFrame, logger: LOGGER) -> None:
    checks = python_libraries(system_requirements)
    print_logger('Python', 'Library', checks, logger)


def python_requirements(system_requirements: pd.DataFrame, logger: LOGGER):
    all_python_distribution(system_requirements, logger)
    all_python_libraries(system_requirements, logger)
