# -*- coding: utf-8 -*-
"""
 Get the range of a partition function
"""

import os
from typing import List
from typing import TYPE_CHECKING

from load_json import load_json
from sql_query import read_query
from sql_schema import get_columns_from_schema

if TYPE_CHECKING:
    from sql_operations import SQLOperations
    from logger import LOGGER


def define_new_range_partition(sql_operations: 'SQLOperations', name_function: str, periodes: List[str],
                              logger: 'LOGGER' = None) -> None:
    path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
    json_data = load_json(os.path.join(path_sql, 'partition.json'), logger=None)

    table_name = '#NewRanges'
    schema = [('Range', 'INT', 'NOT NULL')]
    columns = get_columns_from_schema(schema, logger=logger)

    sql_operations.create_table('#NewRanges', schema)

    format = dict(NameFunction=name_function, TableName=table_name, Columns=", ".join(columns))
    for periode in periodes:
        query = read_query(path_sql, json_data, "is_new_range", format={**format, **{'Range': periode}}, logger=logger)
        sql_operations.execute_query(query)


