# -*- coding: utf-8 -*-
"""
 Fonction open_file
"""

import _io

from logger import LOGGER


def open_file(path: str, mode: str = 'r', encoding='utf-8', logger: LOGGER = None) -> _io.TextIOWrapper:
    try:
        return open(path, encoding=encoding, mode=mode)
    except Exception as e:
        logger.exception(e)
