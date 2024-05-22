# -*- coding: utf-8 -*-
"""
 Lecture du csv des requirement pour production moteur stat
"""

import os
from typing import TYPE_CHECKING

import pandas as pd

from read.read_csv import read_csv
from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def load_system_requirements(variable_environnement: pd.DataFrame, logger: 'LOGGER' = None) -> pd.DataFrame:
    """Load de la table de pilotage requirements.csv

    :param variable_environnement: table des variable d'environnement du système
    :param logger: logs
    :return: DataFrame moteurs_stat
    """
    path_pilotage = get_variable_environnement(variable_environnement, 'pilotage', logger=logger)
    return read_csv(os.path.join(path_pilotage, 'requirements', 'system.csv'), logger=logger)
