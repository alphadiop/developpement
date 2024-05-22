# -*- coding: utf-8 -*-
"""
 Load du fichier json de requêtes
"""

import os
from typing import Dict, Tuple

from load_json import load_json
from logger import LOGGER


def load_sql_queries(path_lib: str, name_lib: str, logger: 'LOGGER' = None) -> Tuple[str, Dict[str, str]]:
    path_sql = os.path.join(path_lib, 'sql_queries')
    return path_sql, load_json(os.path.join(path_sql,  name_lib + '.json'), logger=logger)
