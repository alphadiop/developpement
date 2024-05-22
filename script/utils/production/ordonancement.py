# -*- coding: utf-8 -*-
"""
    Fonctions permettant de logger l' ordonnancement des productions
"""

from typing import TYPE_CHECKING

import pandas as pd

from tabulate_dataframe import tabulate_dataframe

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def write_dataframe_ordonnancement(arbre: dict, logger: 'LOGGER' = None) -> 'DataFrame':
    try:
        level, moteurs = list(), list()
        for key in arbre.keys():
            level.append(key)
            moteurs.append(', '.join(arbre[key]))
        return pd.DataFrame({'Level': level, 'Moteurs': moteurs})
    except Exception as e:
        logger.exception(e)


def write_ordonnancement(logger: 'LOGGER', arbre: dict) -> None:
    df_arbre = write_dataframe_ordonnancement(arbre, logger=logger)

    logger.info("\n\nDéfinition de l'ordonancement des moteurs_locales par niveau: \n")
    logger.info(tabulate_dataframe(df_arbre))
    logger.info('\n'*2)