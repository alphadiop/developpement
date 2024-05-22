# -*- coding: utf-8 -*-
"""
 Fonctions get_moteur
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_moteur_insert_tables(moteurs: 'DataFrame', moteur: str, periodicite: str, logger: 'LOGGER' = None) -> 'DataFrame':
    """Get des lignes de la table de pilotage pour un moteur donn


    :param moteurs:
    :param moteur:
    :param periodicite:
    :param logger:
    :return:
    """
    try:
        return moteurs \
            .query('Moteur == "{0}" & Periodicite == "{1}"'.format(moteur, periodicite))\
            [['Table', 'Table_STAT', 'Version_Source']]
    except Exception as e:
        logger.exception(e)
