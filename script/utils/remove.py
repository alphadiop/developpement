# -*- coding: utf-8 -*-
"""
 Fonction remove
"""

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def remove(path: str, logger: 'LOGGER' = None) -> None:
    """

    :param path:
    :param logger:
    :return: None
    """
    try:
        os.remove(path)
    except Exception as e:
        logger.error(f"Erreur lors du remove de '{path}'")
        logger.exception(e)
