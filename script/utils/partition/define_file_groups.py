# -*- coding: utf-8 -*-
"""
 Définition des différents file group pour construire une partition
"""

from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def define_file_groups(name_table: str, periodes: List[str], logger: 'LOGGER' = None) -> List[str]:
    try:
        file_groups = [define_file_group(name_table, periode) for periode in periodes]
        file_groups.append(name_table)
        return file_groups
    except Exception as e:
        logger.exception(e)


def define_file_group(name_table: str, periode: str, logger: 'LOGGER' = None) -> str:
    try:
        return name_table + periode
    except Exception as e:
        logger.exception(e)
