# -*- coding: utf-8 -*-
"""
 Fonctions get_table_name
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_moteur_source(moteurs: 'DataFrame', moteur: str, periodicite: str, logger: 'LOGGER' = None) -> str:
    """Get du nom du moteur dans les tables moteurs_locales stat


    :param moteurs: table de l'ensemble des moteurs_locales disponibles
    :param moteur: nom du moteur
    :param periodicite: périodicité du moteur
    :param logger: gestionnaire des logs
    :return: nom du moteur
    """
    try:
        return moteurs.query(f"Moteur == '{moteur}' & Periodicite == '{periodicite}'")['Source'].values[0]
    except Exception as e:
        logger.exception(e)
