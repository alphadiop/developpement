# -*- coding: utf-8 -*-
"""
 Get d'une valeur de variables d'environnement
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_variable_environnement(variable_environnement: 'DataFrame', variable: str, logger: 'LOGGER' = None) -> str:
    """Lecture d'une variable d'environnement

    :param variable_environnement: table de l'ensemble des variables d'environnement
    :param variable: variable demandée
    :param logger: gestionnaire des logs
    :return variable d'environnement demandée
    """
    try:
        return variable_environnement.loc[variable].values[0]
    except Exception as e:
        logger.exception(e)
