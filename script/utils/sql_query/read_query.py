# -*- coding: utf-8 -*-
"""
 Fonction read_query: lecture d'une requête SQL d'uns fichier
"""

from typing import TYPE_CHECKING

from get_path_from_json import get_path_from_json
from open_file import open_file

if TYPE_CHECKING:
    from logger import LOGGER


def read_query(path: str, json_data: dict, key: str, format: dict = None, logger: 'LOGGER' = None) -> str:
    """ Lecture à partir d'un fichier d'une requête SQL

    :param path: chemin racine où se trouve les fichiers de requêtes SQL
    :param json_data: nom du fichier contenant la requête SQL
    :param key: clé correspondant à la requête que l'on souhaitte récupérer
    :param format: dictionnaire des variables pour affectation dynamique dans la requête SQL
    :param logger: getionnaire des logs
    :return: requête SQl au format string
    """
    if format is None:
        format = dict()

    try:
        with open_file(get_path_from_json(path, json_data, key, logger=logger), logger=logger) as file:
            query = file.read()
        file.close()
        return ' '.join(query.replace('\n', ' ').split()).format(**format)
    except Exception as e:
        logger.exception(e)
