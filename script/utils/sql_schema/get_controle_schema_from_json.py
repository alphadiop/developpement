# -*- coding: utf-8 -*-
"""
 Get des schema de tables de contrôle SQL à partir d'un fichier JSON de définition
"""

import os
from typing import List, Tuple
from typing import TYPE_CHECKING

from load_json import load_json
from sql_schema import build_schema

if TYPE_CHECKING:
    from logger import LOGGER


def get_controle_schema_from_json(path_schema: str, table: str, logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:
    """
    Get des schémas des tables de contrôle

    :param path_schema: path du dir contenant les données json des tables
    :param table: nom de la table dont on souhaite le schema SQL
    :param logger: gestionnaire des logs
    :return: schema SQL de la table
    """
    json_schema = load_json(os.path.join(path_schema, 'controle', '{0}.json'.format(table)), logger=logger)
    return build_schema(json_schema, format=None, logger=logger)
