# -*- coding: utf-8 -*-
"""
 Load du csv de moteurs_stat.csv
"""

import os
from typing import TYPE_CHECKING

import pandas as pd

from read.read_csv import read_csv
from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def load_moteurs_stat(variable_environnement: 'DataFrame', logger: 'LOGGER' = None) -> 'DataFrame':
    """Load des tables de pilotage moteurs_stat par périodicité (hebdo.csv, mensuel.csv, mensueldebutmois.csv)

    :param variable_environnement: variable d'environnement de la machine de lancement
    :param logger: gestionnaire de logs
    :return: DataFrame moteurs_stat
    """
    moteurs_stat = pd.concat([load_moteur_stat(variable_environnement, 'hebdo', logger=logger),
                              load_moteur_stat(variable_environnement, 'mensuel', logger=logger),
                              load_moteur_stat(variable_environnement, 'mensueldebutmois', logger=logger)],
                             ignore_index=True)
    return moteurs_stat


def update_parameters(logger: 'LOGGER') -> dict:
    """Définition des propiétés utilisées pour la lecture des fichiers csv de propiétés des moteurs_locales

    :param logger: gestionnaire de logs
    :return: dictionnaire de proriétés pour la foncion read_csv
    """
    dtype = {'Moteur': str, 'Table': str, 'Source': str, 'Periodicite': str, 'Profondeur_Historique': str,
             'Profondeur_Periodicite': str, 'Table_STAT': str, 'Table_GersIT': str, 'Table_Relance': str,
             'Version_Source': str}

    parameters = dict(dtype=dtype, usecols=list(dtype.keys()))

    if logger is not None:
        return {**parameters, **{'logger': logger}}
    else:
        return parameters


def load_moteur_stat(variable_environnement: 'DataFrame', periodicite: str, logger: 'LOGGER' = None) -> 'DataFrame':
    """Lecture du fichier de propriétés moteurs_stat pour la périodicité demandée

    :param variable_environnement: variable d'environnement de la machine de lancement
    :param periodicite: [hebdo, mensuel, mensueldebutmois]
    :param logger: gestionnaire de logs
    :return: Dataframe moteurs_stat pour la période demandée
    """
    path_pilotage = get_variable_environnement(variable_environnement, 'pilotage', logger=logger)
    path_moteurs_stat = os.path.join(path_pilotage, 'moteurs_stat')
    moteur_stat = read_csv(os.path.join(path_moteurs_stat, periodicite + '.csv'), **update_parameters(logger))
    moteur_stat.fillna('', inplace=True)
    return moteur_stat
