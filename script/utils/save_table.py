# -*- coding: utf-8 -*-
"""
   Foction générale de sauvegarde des tables moteur statistique
"""
import os
from typing import TYPE_CHECKING
from typing import Union, Dict

import pandas as pd

from copy_file import copy_file
from get_path_data import get_path_data
from get_path_relance import get_path_relance
from make_dirs import make_dirs
from read import read_csv
from write import write_csv
from write import write_json

if TYPE_CHECKING:
    from logger import LOGGER
    from pandas import DataFrame
    from types import GeneratorType


def save_table(df: Union['DataFrame', 'GeneratorType'], path_parameters: Dict[str, str], moteur: str, table: str,
               periodicite: str, periode: str, relance: dict = None, parameters: dict = None,
               logger: 'LOGGER' = None) -> None:
    """Gestion de la sauvegarde en production et en relance

    :param df: dataframe à sauvegarder (data complète si mode production ou data sur panier si mode relance par exemple)
    :param path_parameters: dictionnaire des path du système
    :param moteur: moteur de la table à sauvegarder
    :param table: nom de la table à sauvegarder
    :param periodicite: périodicité de la table
    :param periode: période sauvegardée
    :param relance: dictionnaire des paramètres en mode relance
    :param parameters: paramètres de sauvegarde du fichier
    :param logger: gestionnaire des logs
    :return: None
    """
    format = parameters.get('format', 'csv')
    parameters.pop('format', None)

    if relance is not None:
        logger.info(f"Sauvegarde en mode Relance - '{relance['ModeRelance']}'")
        path_relance = get_path_relance(relance['PathRelance'], relance['ModeRelance'], moteur, periodicite, table,
                                        periode, format=format, logger=logger)

        make_dirs(os.path.join(relance['PathRelance'], moteur, periodicite, periode[:4], periode[-2:]), exist_ok=True,
                  logger=logger)
        if relance['ModeRelance'] in ['correction', 'completion']:
            logger.info(f"Sauvegarde du panier: '{path_relance['Panier']}' - Count: {relance['Panier'].shape[0]}")
            write_csv(relance['Panier'], path_relance['Panier'], logger=logger)
            if format == 'csv':
                logger.info(f"Sauvegarde des données post-relance: '{path_relance['PanierPostRelance']}'")
                write_csv(df, path_relance['PanierPostRelance'], **{**parameters, **{'single_file': True}},
                          logger=logger)

                logger.info(f"Sauvegarde des données hors panier: '{path_relance['DataHorsPanier']}'")
                write_csv(relance['DataHorsPanier'], path_relance['DataHorsPanier'],
                          **{**parameters, **{'single_file': True}}, logger=logger)

                dst_path = os.path.join(path_parameters['save'], table + '.' + format)
                logger.info(f"Copie des données de {path_relance['DataHorsPanier']} à {dst_path}")
                copy_file(path_relance['DataHorsPanier'], dst_path, logger=logger)

                logger.info(f"Ecriture des données post-relance: '{path_relance['PanierPostRelance']}'")
                if not isinstance(df, pd.DataFrame):
                    df = read_csv(path_relance['PanierPostRelance'], dtype=str, chunksize=1000, logger=logger)
                write_csv(df, dst_path, mode='a', header=False, logger=logger)
            elif format == 'json':
                count_post_relance = df.shape[0]
                logger.info(f"Sauvegarde des données post-relance: '{path_relance['PanierPostRelance']}' - "
                            f"Count: {count_post_relance}")
                write_json(df, path_relance['PanierPostRelance'], logger=logger)

                logger.info(f"Sauvegarde des données hors panier: '{path_relance['DataHorsPanier']}'")
                write_json(relance['DataHorsPanier'], path_relance['DataHorsPanier'], logger=logger)

                dst_path = os.path.join(path_parameters['save'], table + '.json')
                logger.info(f"Sauvegarde des données hors panier + post relance: '{dst_path}'")
                relance['DataGlobal'] = relance['DataHorsPanier']
                if count_post_relance > 0:
                    relance['DataGlobal'] = relance['DataGlobal'].append(df)
                write_json(relance['DataGlobal'], dst_path, logger=logger)

        if relance['ModeRelance'] == 'correction':
            if format == 'csv':
                write_csv(relance['DataPanierPreRelance'], path_relance['PanierPreRelance'],
                          **{**parameters, **{'single_file': True}}, logger=logger)
            elif format == 'json':
                write_json(relance['DataPanierPreRelance'], path_relance['PanierPreRelance'], logger=logger)
    else:
        path_data = get_path_data(path_parameters['data'], moteur, periodicite, table, periode, format=format,
                                  logger=logger)

        if parameters is None:
            parameters = dict()

        if format == 'csv':
            write_csv(df, path_data, **parameters, logger=logger)
        elif format == 'json':
            write_json(df, path_data, logger=logger)
