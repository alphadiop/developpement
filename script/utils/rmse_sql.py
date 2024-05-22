# -*- coding: utf-8 -*-
"""
 Calcul du RMSE à partir de requêtes SQL
"""

from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sql_operations import SQLOperations


def rmse_sql(sql_operations: 'SQLOperations', queries: List[str]) -> float:
    """Calcul d'un Root Mean Square Error à partir d'une requête SQL

    :param sql_operations: gestion de la connexion SQL
    :param queries: liste de requêtes
    :return:
    """
    sql_operations.execute_queries(queries)
    numerator = sql_operations.select_table("#Numerator", ['*'])["Numerator"].tolist()[0]
    denominator = sql_operations.select_table("#Denominator", ['*'])["Denominator"].tolist()[0]
    tables = ["#Data_Grouped", "#Numerator", "#Denominator"]
    sql_operations.drop_tables(tables)
    return numerator / denominator
