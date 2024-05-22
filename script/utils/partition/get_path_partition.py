# -*- coding: utf-8 -*-
"""
 Définition du path de sauvegarde d'une partition
"""

import ast
import os
from typing import TYPE_CHECKING

from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_path_partition(variable_environnement: 'DataFrame', path_type: str, name_table: str,
                       logger: 'LOGGER' = None) -> str:
    try:
        paths_partition = get_variable_environnement(variable_environnement, 'path_partition', logger=logger)
        path_partition = ast.literal_eval(paths_partition)[path_type]
        return os.path.join(path_partition, name_table)
    except Exception as e:
        logger.exception(e)
