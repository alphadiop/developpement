# -*- coding: utf-8 -*-
"""
 Load du csv de variable d'environnement
"""

import os
from pathlib import Path
from typing import TYPE_CHECKING

from read import read_csv

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def load_variable_environnement(logger: 'LOGGER' = None) -> 'DataFrame':
    try:
        return read_csv(os.path.join(Path(os.path.dirname(__file__)).parent.parent.parent,
                                     'variable_environnement.csv'), index_col=0)
    except Exception as e:
        logger.exception(e)

# if __name__=="__main__":
#     path = Path(os.path.dirname(__file__)).parent.parent.parent
#     print(f"path : {path}")