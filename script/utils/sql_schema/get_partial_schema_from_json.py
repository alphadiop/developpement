# -*- coding: utf-8 -*-
"""
 Get des schema partiels de tables SQL à partir d'un fichier JSON de définition et d'une liste de colonnne
"""

from typing import List
from typing import TYPE_CHECKING
from typing import Tuple

from sql_schema import get_schema_from_json

if TYPE_CHECKING:
    from logger import LOGGER


def get_partial_schema_from_json(path_schema: str, table: str, periodicite: str,
                                 columns: List[str], logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:
    schema = get_schema_from_json(path_schema, table, periodicite, logger=logger)
    return list(filter(lambda tp: tp[0] in columns, schema))
