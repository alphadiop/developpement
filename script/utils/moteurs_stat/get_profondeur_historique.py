# -*- coding: utf-8 -*-
"""
 Fonctions get_profondeur_historique
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame
    from logger import LOGGER


def get_profondeur_historique(moteurs_stat: 'DataFrame', moteur: str, periodicite: str, logger: 'LOGGER' = None) -> str:
    """Get du nom de la table de chargement dans le DW

    :param moteurs_stat: table de propiétés de les moteurs_locales moteur_stat
    :param moteur: moteur dont on veut connaître la table de destination dans le DW
    :param periodicite: périodiciteé du moteur
    :param logger: gestionnaire des logs
    :return: nom de la table SQL
    """
    try:
        return (moteurs_stat
                .query('Moteur == "{0}" & Periodicite == "{1}"'.format(moteur, periodicite))[['Moteur', 'Profondeur_Historique']]
                .drop_duplicates()['Profondeur_Historique'].values[0])
    except Exception as e:
        logger.exception(e)
