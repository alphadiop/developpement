# -*- coding: utf-8 -*-
"""
    Définition de la liste des tables figees utilisees dans les moteurs_locales
"""

import os
from typing import List
from typing import TYPE_CHECKING

from variable_environnement import get_variable_environnement
from variable_environnement import load_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def get_list_data_figees(variable: str, logger: 'LOGGER' = None) -> List[str]:
    try:
        variable_environnement = load_variable_environnement(logger=logger)
        path_data_figees = get_variable_environnement(variable_environnement, variable, logger=logger)
        return list(map(lambda x: x.split('.')[0], os.listdir(path_data_figees)))
    except Exception as e:
        logger.exception(e)

