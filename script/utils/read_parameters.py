# -*- coding: utf-8 -*-
"""
 Fonction read_parameters
"""

import ast


def read_parameters(argv: list) -> dict:
    """Lecture des paramètres données à une exécution d'un script python

    :param argv: liste  des arguments
    :return: premier argument
    """
    # Lecture des paramètres d'entrées
    return ast.literal_eval(argv[1])
