# -*- coding: utf-8 -*-
"""
 Construction des differents paramètres nécessaire à une partition de table SQL
"""

from typing import TYPE_CHECKING
from typing import Tuple

if TYPE_CHECKING:
    from logger import LOGGER


def get_attribut_partition(table_dw: str, logger: 'LOGGER' = None) -> Tuple[str, str, str, str]:
    try:
        _, _, name_table = get_attribut_table(table_dw, logger=logger)
        name_function = 'PF' + name_table
        name_scheme = 'PS' + name_table
        name_index = 'Index_' + name_table
        return name_table, name_function, name_scheme, name_index
    except Exception as e:
        logger.exception(e)


def get_attribut_table(table_dw: str, logger: 'LOGGER' = None) -> Tuple[str, str, str]:
    try:
        table_split = table_dw.replace(']', '').replace('[', '').split('.')
        name_base = table_split[0]
        name_schema = table_split[1]
        name_table = table_split[2]
        return name_base, name_schema, name_table
    except Exception as e:
        logger.exception(e)
