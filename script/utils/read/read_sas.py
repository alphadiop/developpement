# -*- coding: utf-8 -*-
"""
 Fonction read_sas: lecture d'une table sas
"""

from typing import Union
from typing import TYPE_CHECKING
import pandas as pd

if TYPE_CHECKING:
    from logger import LOGGER


def read_sas(path: str, format: str = 'sas7bdat', encoding: str = None, chunksize: int = None,
             logger: 'LOGGER' = None) -> Union[pd.DataFrame, pd.io.parsers.TextFileReader]:
    """Lecture de la table SAS

    Parameters
    ----------
    :param path : Chemin du fichier à lire
    :param format: SAS format (default 'sas7bdat')
    :param encoding: encodage pour le texte
    :param chunksize: default value int(1e6)
    :param logger: variable de la class LOGGER (gestion des logs)
    :return DataFrame
    """
    try:
        return pd.read_sas(path, format=format, encoding=encoding, chunksize=chunksize)
    except FileNotFoundError:
        logger.error("Le fichier '{0}' n'existe pas".format(path))
