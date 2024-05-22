# -*- coding: utf-8 -*-
"""
 Get de la table en lien avec les calls
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame
    from logger import LOGGER


def get_table_calls(tables_calls: 'DataFrame', moteur: str, table: str, logger: 'LOGGER' = None) -> str:
    try:
        return tables_calls.query(f'Moteur == "{moteur}" & Table == "{table}"')['Table_STAT'].values[0]
    except Exception as e:
        logger.exception(e)
