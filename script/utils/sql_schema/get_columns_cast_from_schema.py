# -*- coding: utf-8 -*-
"""
 Get des noms de colonnes à partir d'un schema SQL
"""

from typing import List, Tuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_columns_cast_from_schema(schema: List[Tuple[str, str, str]], logger: 'LOGGER' = None) -> List[str]:
    """Get des noms de colonnes à partir d'un schema SQL

    :param schema: schema SQL
    :param logger: gestion de logs
    :return: liste des noms de colonnes
    """
    try:
        cast = 'CAST(CAST({0} AS {1}) AS NVARCHAR(100)) AS {0}'
        return [cast.format(tp[0], tp[1]) for tp in schema]
    except Exception as e:
        logger.exception(e)
