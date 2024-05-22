# -*- coding: utf-8 -*-
"""
 Get des noms de colonnes à partir d'un schema SQL
"""

from typing import List, Tuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_columns_from_schema(schema: List[Tuple[str, str, str]], logger: 'LOGGER' = None) -> List[str]:
    """Get des noms de colonnes à partir d'un schema SQL

    :rtype: List[str]
    :param schema: schema SQL
    :param logger: gestion de logs
    :return: liste des noms de colonnes
    """
    try:
        return [tp[0] for tp in schema]
    except Exception as e:
        logger.exception(e)
