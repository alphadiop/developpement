# -*- coding: utf-8 -*-
"""
 Fonctions get_table_name
"""

from typing import TYPE_CHECKING

from variable_environnement import get_variable_environnement
from variable_environnement import load_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame


def get_table_name(moteurs_stat: 'DataFrame', table: str, periodicite: str, is_production: bool = False,
                   is_relance: bool = False, logger: 'LOGGER' = None) -> str:
    """Get du nom de la table de chargement sur la base DW_GersIT ou sur la base STAT

    :param moteurs_stat: dataframe de propriétés des moteurs_locales stat
    :param table: nom de la table dont on souhaite avoir la table SQL de chargement
    :param periodicite: périodicité de la table
    :param is_production: paramètre permettant de choisir entre la base STAT
    :param is_relance: paramètre permettant de choisir la base Relance
    :param logger: gestionnaire des logs
    :return: nom de la table SQL
    """
    try:
        moteurs_stat_filtered = moteurs_stat.query('Table == "{0}" & Periodicite == "{1}"'.format(table, periodicite))
        if is_production:
            return moteurs_stat_filtered['Table_STAT'].values[0]
        elif is_relance:
            return moteurs_stat_filtered['Table_Relance'].values[0]
        else:
            table = moteurs_stat_filtered['Table_GersIT'].values[0]
            if table.split('.')[0] == '[DW_GersIt]':
                variable_environnement = load_variable_environnement(logger=logger)
                serveur = get_variable_environnement(variable_environnement, 'server_source', logger=logger)
                table = '.'.join([serveur, table])
            return table
    except Exception as e:
        logger.exception(e)
