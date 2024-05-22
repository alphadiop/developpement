# -*- coding: utf-8 -*-
"""
 Vérification de l'ensemble des prerequis système (Python, SQL et R)
"""

from typing import TYPE_CHECKING

from requirements.load_system_requirements import load_system_requirements
from requirements.python_requirements import python_requirements
from requirements.r_requirements import r_requirements
from requirements.sql_requirements import sql_requirements
from variable_environnement import load_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def requirements(logger: 'LOGGER'):

    variable_environnement = load_variable_environnement(logger=logger)
    system_requirements = load_system_requirements(variable_environnement, logger=logger)

    sql_requirements(variable_environnement, logger)
    python_requirements(system_requirements, logger)
    r_requirements(system_requirements, logger)


if __name__ == '__main__':

    from get_logger import get_logger
    from statistique import STATISTIQUE

    path_log = STATISTIQUE.get_path_log()

    logger = get_logger({'Moteur': 'requirements', 'Periodicite': 'hebdo', 'Periode': '201901'},
                        STATISTIQUE.get_path_log(), type_logger="stream", format='')

    requirements(logger)
