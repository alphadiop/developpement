# -*- coding: utf-8 -*-
"""
    Définition des path de sauvegarde en mode de relance
"""

import os
from typing import Dict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_path_relance(path_relance: str, mode_relance: str, moteur: str, periodicite: str, table: str, periode: str,
                     format: str = 'csv', logger: 'LOGGER' = None) -> Dict[str, str]:
    """Définition des paths de sauvegarde en mode relance

    :param path_relance: path racine de sauvegarde
    :param mode_relance: mode de relance
    :param moteur:
    :param periodicite:
    :param table:
    :param periode:
    :param format:
    :param logger: gestionnaire de relance
    :return: dictionnaire de paths
    """
    try:
        path = dict()
        path_root = os.path.join(path_relance, moteur, periodicite, periode[:4], periode[-2:])
        if mode_relance in ['correction', 'completion']:
            path['Panier'] = os.path.join(path_root, 'panier_presentation.csv')
            path['PanierPostRelance'] = os.path.join(path_root, '{0}_panier_post_relance.{1}'.format(table, format))
            path['DataHorsPanier'] = os.path.join(path_root, '{0}_hors_panier.{1}'.format(table, format))
        if mode_relance == 'correction':
            path['PanierPreRelance'] = os.path.join(path_root, '{0}_panier_pre_relance.{1}'.format(table, format))
        return path
    except Exception as e:
        logger.exception(e)
