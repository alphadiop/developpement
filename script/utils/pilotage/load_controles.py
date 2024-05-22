# -*- coding: utf-8 -*-
"""
 Load du json de contrôle table moteurs_locales
"""

import os
from typing import TYPE_CHECKING

import pandas as pd

from load_json import load_json
from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def load_controles(variable_environnement: pd.DataFrame, data: str, logger: 'LOGGER' = None) -> dict:
    """
    Chargement de l'ensemble des données relatives au contrôles des tables

    :param variable_environnement:
    :param data: nom des données à charger
    :param logger: gestion des logs
    :return: opérations de contrôles par tables
    """
    path_pilotage = get_variable_environnement(variable_environnement, 'pilotage', logger=logger)
    path_controle = os.path.join(path_pilotage, 'controle', '{0}.json'.format(data))
    return load_json(path_controle, logger=logger)
