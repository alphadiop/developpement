# -*- coding: utf-8 -*-
"""
    Fonction de définition de l'ensemble des paramètres de production
"""

from typing import Dict
from typing import Union


def set_parameters_production(parameters: Dict[str, Union[str, bool]],
                              is_production: bool, is_reprise: bool, is_relance: bool) -> Dict[str, Union[str, bool]]:
    """Set des paramtres de production dans le dictionnaire etude_parameters

    :param parameters: dictionnaire de paramètres de la class de production
    :param is_production: boolean True si production
    :param is_reprise: boolean True si reprise
    :param is_relance: boolean True si relance

    :return dictionnaire de parametres augmenté des paramètres de production
    """
    parameters['IsProduction'] = is_production
    parameters['IsReprise'] = is_reprise
    parameters['IsRelance'] = is_relance

    return parameters
