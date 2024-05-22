# -*- coding: utf-8 -*-
"""
 Get des dates de début et de fin d'une étude hebdomadaire ou mensuelle
"""

import os
from datetime import datetime
from typing import TYPE_CHECKING
from typing import Tuple

from load_json import load_json
from sql_query import read_query
from time_periodes import get_cle_periode

if TYPE_CHECKING:
    from logger import LOGGER
    from sql_operations import SQLOperations


def get_range_date(sql_operations: 'SQLOperations', periodicite: str, periode: str, logger: 'LOGGER' = None) -> Tuple[str, str]:
    """Définit la date min et max pour une période et une périodicité donnée

    :param sql_operations: variable de type SQLOperations
    :param periodicite: periodicite de la période [mensuel, mensueldebutmois, hebdo]
    :param periode: période dont on veut déterminer le range de dates
    :param logger: gestionnaire des logs
    :return: Tuple (date de début, date de fin)
    """
    try:
        path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
        json_data = load_json(os.path.join(path_sql, 'time_periodes.json'), logger=logger)

        query = read_query(path_sql, json_data, "get_range_date",
                           format=dict(ClePeriode=get_cle_periode(periodicite, logger=logger), Periode=periode),
                           logger=logger)
        df = sql_operations.load_df(query)

        for column in ['DateDebut', 'DateFin']:
            df[column] = df.apply(lambda row: datetime.strftime(row[column], "%Y-%m-%d"), axis=1)

        return df.to_dict()["DateDebut"][0], df.to_dict()["DateFin"][0]
    except Exception as e:
        logger.exception(e)

