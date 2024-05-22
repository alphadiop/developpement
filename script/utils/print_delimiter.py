# -*- coding: utf-8 -*-
"""
 Fonction print dans les logs de delimiter "="
"""

from logger import LOGGER


def print_delimiter(logger: LOGGER) -> None:
    """
    Print de delimiter dans les logs

    :param logger: class LOGGER
    :return: None
    """
    logger.info("=" * 121)
