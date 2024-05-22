# -*- coding: utf-8 -*-
"""
 Fonctions get_table_name
"""

import pandas as pd

from logger import LOGGER


def get_moteur_name(moteurs: pd.DataFrame, table: str, periodicite: str, logger: LOGGER = None) -> str:
    """Get du nom du moteur dans les tables moteurs_locales stat


    :param moteurs:
    :param table:
    :param periodicite:
    :param logger:
    :return:
    """
    try:
        return moteurs.query('Table == "{0}" & Periodicite == "{1}"'.format(table, periodicite))['Moteur'].values[0]
    except Exception as e:
        logger.exception(e)
