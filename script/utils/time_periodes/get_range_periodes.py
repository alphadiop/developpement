# -*- coding: utf-8 -*-
"""
    Définition d'un intervalle de temps comme une liste triée par ordre croissant de CleSemaineISOStatistique ou
    CleMoisAnnee
"""

import os
from typing import List
from typing import TYPE_CHECKING

from load_json import load_json
from sql_query import read_query
from time_periodes import get_cle_periode

if TYPE_CHECKING:
    from sql_operations import SQLOperations
    from logger import LOGGER


path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
json_data = load_json(os.path.join(path_sql, 'time_periodes.json'), logger=None)


def get_semaines(sql_operations: 'SQLOperations', start_period: str, end_period: str, logger: 'LOGGER' = None) -> List[str]:
    """Get de la liste de numéro de semaine iso compris entre deux semaines iso. Triée par ordre croissant

    :param sql_operations: connexion au serveur sql
    :param start_period: début de la période
    :param end_period: fin de la période
    :param logger: gestion de logs
    :return: liste de CleSemaineISOStatistique
    """
    cle_periode = get_cle_periode('hebdo', logger=logger)
    return get_periodes(sql_operations, start_period, end_period, cle_periode, logger=logger)


def get_mois(sql_operations: 'SQLOperations', start_period: str, end_period: str, logger: 'LOGGER' = None) -> List[str]:
    """Get de la liste de numéro de cle mois annee compris entre deux mois. Trié par ordre corissant

    :param sql_operations: connexion au serveur sql
    :param start_period: début de la période
    :param end_period: fin de la période
    :param logger: gestion de logs
    :return: liste de CleMoisAnnee
    """
    cle_periode = get_cle_periode('mensuel', logger=logger)
    return get_periodes(sql_operations, start_period, end_period, cle_periode, logger=logger)


def get_periodes(sql_operations: 'SQLOperations', start_period: str, end_period: str, cle_periode: str,
                 logger: 'LOGGER' = None):
    query = read_query(path_sql, json_data, "get_periodes",
                       format=dict(StartPeriode=start_period, EndPeriode=end_period, ClePeriode=cle_periode),
                       logger=logger)
    periodes = sql_operations.load_df(query)[cle_periode].values
    periodes = list(map(str, periodes))
    return sorted(periodes)
