# -*- coding: utf-8 -*-
"""
 Get des différentes range sur la colonne à partitionner
"""

from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sql_operations import SQLOperations


def distinct_range(sql_operations: 'SQLOperations', src_table: str, column: str) -> List[str]:
    periodes = sql_operations.select_table(src_table, [column], distinct=True)[column].values
    return sorted(map(lambda periode: str(periode), periodes))
