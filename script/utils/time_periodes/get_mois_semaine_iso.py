# -*- coding: utf-8 -*-
"""
 Récupération des numéro de semaines iso pour un mois donné
"""

import os
from typing import List
from typing import TYPE_CHECKING

from load_json import load_json
from sql_query import read_query

if TYPE_CHECKING:
    from logger import LOGGER
    from sql_operations import SQLOperations


def get_mois_semaine_iso(sql_operations: 'SQLOperations', cle_mois_annee: str, logger: 'LOGGER' = None) -> List[str]:
    """Get des numéros de semaine ISO d'un mois donné

    :param sql_operations: variable de type SQLOperations
    :param cle_mois_annee: mois
    :param logger: gestion des logs
    :return: Liste des numéros de semaines ISO du mois
    """
    try:
        path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
        json_data = load_json(os.path.join(path_sql, 'time_periodes.json'), logger=logger)

        query = read_query(path_sql, json_data, "get_semaines_mois", format=dict(CleMoisAnnee=cle_mois_annee),
                           logger=logger)

        cle_semaine_iso = sorted(sql_operations.load_df(query)["SemaineISO"].values.tolist())

        return list(map(lambda x: str(x), cle_semaine_iso))

    except Exception as e:
        logger.exception(e)
