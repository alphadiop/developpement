# -*- coding: utf-8 -*-
"""
 Fonction read_queries
"""

from typing import List

from get_path_from_json import get_path_from_json
from logger import LOGGER
from open_file import open_file


def read_queries(path: str, json_data: dict, key: str, format: dict = None, logger: LOGGER = None) -> List[str]:
    """Lecture à partir d'un fichier d'une liste de requête SQL

    :param path: chemin racine où se trouve les fichiers de requêtes SQL
    :param json_data: nom du fichier contenant les requêtes SQL
    :param key: clé correspondant à la requête que l'on souhaitte récupérer
    :param format: dictionnaire des variables pour affectation dynamique dans la requête SQL
    :param logger: getionnaire des logs
    :return: liste de requêtes SQl au format string
    """
    if format is None:
        format = dict()

    try:
        with open_file(get_path_from_json(path, json_data, key, logger), logger=logger) as file:
            list_query = [' '.join(query.replace('\n', ' ').split()) for query in file.read().split("\n\n")]
        file.close()
        return [query.format(**format) for query in list_query]
    except Exception as e:
        logger.exception(e)
