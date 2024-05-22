# -*- coding: utf-8 -*-
"""
 Fonction get_path_data
"""
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_path_data(path_data: str, moteur: str, periodicite: str, table: str, periode: str, format: str = 'csv',
                  logger: 'LOGGER' = None) -> str:
    """Get du path d'une table pour une période donnée

    :param path_data: path de sauvegarde des résultats des moteurs_locales
    :param moteur: nom du moteur
    :param periodicite: hebdomadaire ou mensuelle
    :param table: nom de la table
    :param periode: periode (CleSemaineISOAnneeStatistique ou CleMoisAnnee)
    :param format: format du fichier de sortie (csv, json...)
    :param logger: gestion des logs
    :return: path de la table
    """
    try:
        path_dir = os.path.join(path_data, moteur, periodicite, periode[:4], periode[-2:])
        if table == 'sognow':
            if periodicite == 'hebdo':
                return os.path.join(path_dir, f"SOG_CONSEIL_WEEK_{periode}.csv")
            elif periodicite == 'mensueldebutmois':
                return os.path.join(path_dir, f"SOG_CONSEIL_MONTH_{periode}.csv")
        else:
            return os.path.join(path_dir, table + '.' + format)
    except Exception as e:
        logger.exception(e)
