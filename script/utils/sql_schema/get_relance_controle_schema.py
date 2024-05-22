# -*- coding: utf-8 -*-
"""
 Get des schema de tables de contrôle pour le mode de relance
"""

from typing import List, Tuple
from typing import TYPE_CHECKING

from sql_schema import get_controle_schema_from_json

if TYPE_CHECKING:
    from logger import LOGGER


def get_relance_controle_schema(path_schema: str, table: str, logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:
    """
    Get des schémas des tables de contrôle pour le mode relance

    :param path_schema: path du dir contenant les données json des tables
    :param table: nom de la table dont on souhaite le schema SQL
    :param logger: gestionnaire des logs
    :return: schema SQL de la table
    """
    schema = get_controle_schema_from_json(path_schema, table, logger=logger)
    return [('IdRelance', 'INT', 'NOT NULL')] + schema + [('Data', 'TINYINT', 'NOT NULL')]
