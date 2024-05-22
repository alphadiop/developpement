# -*- coding: utf-8 -*-
"""
 Fonction get_logger
"""

from logger import LOGGER


def get_logger(parameters: dict, path_log: str, type_logger: str = "stream_file", format: str = None) -> 'LOGGER':
    return LOGGER(parameters, path_log, type_logger=type_logger, format=format)
