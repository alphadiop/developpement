# -*- coding: utf-8 -*-
"""
 Load des tables de prérequis des moteurs_locales stat
"""

import os
from typing import TYPE_CHECKING

import pandas as pd

from read import read_csv
from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER

all_columns = {'data_figees': ['Periodicite', 'Moteur', 'Fichier', 'Extension'],
               'data_moteur_statistique': ['Periodicite', 'Moteur', 'Source', 'SourcePeriodicite', 'Table',
                                           'Profondeur'],
               'sql_moteur_statistique': ['Periodicite', 'Moteur', 'Source', 'SourcePeriodicite', 'Profondeur']}


def load_prerequis(variable_environnement: pd.DataFrame, periodicite: str, fichier: str, logger: 'LOGGER' = None) -> pd.DataFrame:
    """Load des tables de pilotage de prerequis

    :param variable_environnement: table des variables d'environnement du système
    :param periodicite: périodicité dont on souhaite obtenir la liste des prérequis
    :param fichier: type de prérequis ['data_figees', 'data_moteur_statistique', 'sql_moteur_statistique']
    :param logger: gestionnaire des logs
    :return: DataFrame des prerequis
    """
    try:
        columns = all_columns[fichier]
        if (periodicite == 'mensueldebutmois') and (fichier == 'sql_moteur_statistique'):
            columns += ['Concatenation']
        dtype = {column: str for column in columns}
        parameters = dict(dtype=dtype, usecols=list(dtype.keys()), logger=logger)
        path_prerequis = os.path.join(get_variable_environnement(variable_environnement, 'pilotage'), 'prerequis',
                                      periodicite.lower())
        return read_csv(os.path.join(path_prerequis, fichier + '.csv'), **parameters)
    except Exception as e:
        logger.exception(e)


