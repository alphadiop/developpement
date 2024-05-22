
from typing import Tuple, List

import pandas as pd
import rpy2.robjects as robjects

from logger import LOGGER
from requirements.compare_version import compare_version
from requirements.print_logger import print_logger


def r_requirements(system_requirements: pd.DataFrame, logger: LOGGER):
    all_r_distribution(system_requirements, logger)
    all_r_libraries(system_requirements, logger)


def all_r_distribution(system_requirements: pd.DataFrame, logger: LOGGER) -> None:
    checks = r_distribution(system_requirements)
    print_distribution(checks, logger)


def r_distribution(system_requirements: pd.DataFrame) -> List[Tuple[str, str, str, str]]:
    version_requis = (system_requirements[(system_requirements.Language == 'R') & (system_requirements.Library == 'distribution')]['Requirement']
                      .values.tolist()[0])

    version_actuel = list(robjects.r("R.version.string"))[0].split(' ')[2]

    return [('R', version_requis, version_actuel, 'OK' if compare_version(version_actuel, version_requis) else 'NOOK')]


def print_distribution(checks: List[Tuple[str, str, str, str]], logger: LOGGER):
    logger.info('\n\nR distribution:')

    headers = (' Distribution ', ' Requis ', ' Actuel ', ' ')

    format = {head: max([len(head)] + [len(check[ind]) for check in checks]) for ind, head in enumerate(headers)}

    logger.info('\n')
    logger.info('  |' + '|'.join([head.center(format[head], ' ') for head in format.keys()]) + '|')
    logger.info('  |' + '|'.join(['-'*format[head] for head in format.keys()]) + '|')

    for check in checks:
        logger.info('  |' + '|'.join([check[ind].center(format[head]) for ind, head in enumerate(headers)]) + '|')


def r_libraries(system_requirements: pd.DataFrame) -> List[Tuple[str, str, str, str]]:
    libraries_version = system_requirements[(system_requirements.Language == 'R') & (system_requirements.Library != 'distribution')][['Library', 'Requirement']]
    libraries_version.set_index('Library', inplace=True)

    checks = list()
    for row in libraries_version.itertuples():
        version_requis = libraries_version.loc[row.Index].Requirement
        if list(robjects.r(""""{0}" %in% rownames(installed.packages())""".format(row.Index)))[0]:
            version_actuel = ".".join(map(lambda x: str(x), list(list(robjects.r("""packageVersion("{0}")""".format(row.Index)))[0])))
            checks.append((row.Index, version_requis, version_actuel,
                           'OK' if compare_version(version_actuel, version_requis) else 'NOOK'))
        else:
            checks.append((row.Index, version_requis, '?', 'NOOK'))

    return checks


def all_r_libraries(system_requirements: pd.DataFrame, logger: LOGGER) -> None:
    checks = r_libraries(system_requirements)
    print_logger('R', 'Library', checks, logger)
