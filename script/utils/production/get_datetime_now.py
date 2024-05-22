# -*- coding: utf-8 -*-
"""
    Fonction get_datetime_now
"""

import datetime


def get_datetime_now() -> str:
    """Fonction retournant le timestamp de l'instant sous forme str

    :return: now timestamp
    """
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
