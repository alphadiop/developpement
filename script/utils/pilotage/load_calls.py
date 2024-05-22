# -*- coding: utf-8 -*-
"""
 Load du csv des propriétés des tables des calls
"""
import os
from typing import TYPE_CHECKING

from read import read_csv
from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from pandas import DataFrame
    from logger import LOGGER


def load_calls(variable_environnement: 'DataFrame', logger: 'LOGGER' = None) -> 'DataFrame':
    """Lecture du fichier de propriétés moteurs_stat pour la périodicité demandée

    :param variable_environnement: variable d'environnement de la machine de lancement
    :param logger: gestionnaire de logs
    :return: Dataframe moteurs_stat pour la période demandée
    """
    path_pilotage = get_variable_environnement(variable_environnement, 'pilotage', logger=logger)
    path_calls = os.path.join(path_pilotage, 'calls', 'calls.csv')
    return read_csv(path_calls, logger=logger)
