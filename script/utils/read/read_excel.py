# -*- coding: utf-8 -*-
"""
 Fonctions de lecture de fichier excel
"""

from typing import TYPE_CHECKING
from typing import Union, List, Dict, Type

import pandas as pd

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def read_excel(path: str, sheet_name: Union[int, str] = 0, usecols: List[str] = None,
               dtype: Union[Dict[str, str], Type[str]] = None, logger: 'LOGGER' = None) -> 'DataFrame':
    """Lecture de fichier au format csv

    Parameters
    ----------
    :param path : Chemin du fichier à lire
    :param sheet_name: nom de la sheet à lire
    :param usecols: liste des colonnes à extraire
    :param dtype: types des colonnes
    :param logger: variable de la class LOGGER (gestion des logs)
    :return pandas dataframe
    """
    try:
        return pd.read_excel(path, sheet_name=sheet_name, usecols=usecols, dtype=dtype, header=0)
    except Exception as e:
        logger.error("Fichier lu au moment de l'exception: {0}".format(path))
        logger.exception(e)
