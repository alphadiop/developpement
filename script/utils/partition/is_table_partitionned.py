# -*- coding: utf-8 -*-
"""
 Check if a SQL table is partitionned
"""

import os
from typing import TYPE_CHECKING

from load_json import load_json
from sql_query import read_query

if TYPE_CHECKING:
    from sql_operations import SQLOperations
    from logger import LOGGER


def is_table_partitionned(sql_operations: 'SQLOperations', name_table: str, logger: 'LOGGER' = None) -> bool:
    path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
    json_data = load_json(os.path.join(path_sql, 'partition.json'), logger=logger)

    query = read_query(path_sql, json_data, "is_table_partitionned", format=dict(NameTable=name_table),
                       logger=logger)
    table_partionned = sql_operations.load_df(query)
    return table_partionned.shape[0] == 1
