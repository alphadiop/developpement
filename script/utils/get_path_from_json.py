# -*- coding: utf-8 -*-
"""
 Fonction get_path_from_json
"""

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_path_from_json(path: str, json_data: dict, key: str, logger: 'LOGGER' = None) -> str:
    """Get du path des requête à partir du join(path + json_data[key])

    :param path: root path
    :param json_data: dictionnary key: path requêtes sql
    :param key: key du json_data dic
    :param logger: geston des logs
    :return: path
    """
    try:
        return os.path.join(path, json_data[key])
    except Exception as e:
        logger.exception(e)
