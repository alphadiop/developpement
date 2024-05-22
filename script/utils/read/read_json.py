# -*- coding: utf-8 -*-
"""
 Fonctions de lecture de fichier json - DataFrame Pandas ou Dask
"""

from typing import List
from typing import TYPE_CHECKING
from typing import Union

import dask.dataframe as dd
import pandas as pd

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame as pandas_dataframe
    from dask.dataframe import DataFrame as dask_dataframe
    from types import GeneratorType


def read_json(path: Union[str, List[str]], orient: str = "records", lines: bool = False, format: str = 'pandas',
              npartitions: int = None, logger: 'LOGGER' = None) \
        -> Union['pandas_dataframe', 'dask_dataframe', 'GeneratorType']:
    try:
        if format == 'pandas':
            return pd.read_json(path, orient=orient, lines=lines)
        elif format == 'dask':
            df = dd.read_json(path, orient=orient, lines=lines)
            if npartitions is not None:
                df = df.repartition(npartitions=npartitions)
            return df
    except Exception as e:
        logger.error("Fichier lu au moment de l'exception: {0}".format(path))
        logger.exception(e)
