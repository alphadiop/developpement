# -*- coding: utf-8 -*-
"""
 Fonctions get_profondeur_periodicite
"""

import pandas as pd

from logger import LOGGER


def get_profondeur_periodicite(moteurs: pd.DataFrame, moteur: str, periodicite: str, logger: LOGGER = None) -> str:
    """Get du nom de la table d'insertion dans le DW


    :param moteurs:
    :param moteur:
    :param periodicite:
    :param logger:
    :return:
    """
    try:
        return moteurs.query('Moteur == "{0}" & Periodicite == "{1}"'.format(moteur, periodicite))[['Moteur', 'Profondeur_Periodicite']].drop_duplicates()['Profondeur_Periodicite'].values[0]
    except Exception as e:
        logger.exception(e)
