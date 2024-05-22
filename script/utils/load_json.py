# -*- coding: utf-8 -*-
"""
 Fonction load_json
"""

import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def load_json(path: str, logger: 'LOGGER' = None) -> dict:
    """Chargement d'un fichier JSON

    :param path: chemin d'un fichier JSON
    :param logger: gestion des logs
    :return: dictionnaire du contenu du fichier JSON chargée
    """
    try:
        with open(path) as f:
            json_data = json.load(f)
        f.close()
        return json_data
    except Exception as e:
        logger.exception(e)
