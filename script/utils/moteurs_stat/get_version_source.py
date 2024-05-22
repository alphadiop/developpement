# -*- coding: utf-8 -*-
"""
 Fonctions get_version_source
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_version_source(moteurs_stat: 'DataFrame', table: str, periodicite: str, logger: 'LOGGER' = None) -> str:
    """

    :param moteurs_stat: dataframe des moteurs_locales stats
    :param table: nom de la table considérée
    :param periodicite: périodicité considérée
    :param logger: gestion des logs
    :return: version source [string]
    """
    try:
        version_source = (moteurs_stat.query('Table == "{0}" & Periodicite == "{1}"'.format(table, periodicite))
                          ['Version_Source'].values[0])
        return str(version_source)
    except Exception as e:
        logger.exception(e)
