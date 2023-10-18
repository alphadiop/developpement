# -*- coding: utf-8 -*-
"""
 Fonctions de lecture de fichier csv - DataFrame Pandas ou Dask
"""

import types
from typing import TYPE_CHECKING
from typing import Type
from typing import Union

import dask.dataframe as dd
import pandas as pd

if TYPE_CHECKING:
    from logger import LOGGER


def read_csv(path: str, format: str = 'pandas', sep: str = ",", encoding: str = 'utf-8-sig',
             dtype: Union[dict, Type[str]] = None, usecols: list = None, index_col: int = None, decimal: str = '.',
             blocksize: int = 64000000, chunksize: int = None,
             logger: 'LOGGER' = None) -> Union[pd.DataFrame, types.GeneratorType]:
    """Lecture fichier au format csv

    :param path : Chemin du fichier à lire
    :param format: Format du dataframe ('pandas' [default] or dask)
    :param sep: séparateur du fichier csv
    :param encoding: encodage à utiliser (optionnel default UTF-8)
    :param dtype: dictionnaire du type des colonnes du fichier csv (optionnel - default None)
    :param usecols: liste des colonnes à sélectioner
    :param index_col: index de la colonne à utiliser comme  index du dataframe
    :param decimal: caractère de definition des decimales
    :param blocksize: Number of bytes by which to cut up larger files
    :param chunksize:
    :param logger: variable de la class LOGGER (gestion des logs)

    :return pandas dataframe
    """
    try:
        if format == 'pandas':
            return pd.read_csv(path, header=0, sep=sep, encoding=encoding, dtype=dtype, usecols=usecols,
                               decimal=decimal, chunksize=chunksize, index_col=index_col)
        elif format == 'dask':
            return dd.read_csv(path, sep=sep, dtype=dtype, usecols=usecols, encoding=encoding, blocksize=blocksize)
    except Exception as e:
        logger.error("Fichier lu au moment de l'exception: {0}".format(path))
        logger.exception(e)


