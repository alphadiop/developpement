# -*- coding: utf-8 -*-
"""
 Get du mois pour un numéro de semaine iso donnée
"""

import os
from typing import TYPE_CHECKING

from sql_query import load_sql_queries
from sql_query import read_query

if TYPE_CHECKING:
    from logger import LOGGER
    from sql_operations import SQLOperations


def get_semaine_iso_mois(sql_operations: 'SQLOperations', cle_iso_week: str, logger: 'LOGGER' = None) -> str:
    """Get de la cle mois annee pour une cle semaine iso

    :param sql_operations: variable de type SQLOperations
    :param cle_iso_week: cle semaine iso annee statistique
    :param logger: gestion des logs
    :return: cle mois annee
    """
    try:
        path_sql, json_data = load_sql_queries(os.path.dirname(__file__), 'time_periodes', logger=logger)
        query = read_query(path_sql, json_data, "get_cle_mois_annee", format=dict(Periode=cle_iso_week), logger=logger)
        return str(sql_operations.load_df(query).iloc[0]['CleMoisAnnee'])
    except Exception as e:
        logger.exception(e)
