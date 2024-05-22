# -*- coding: utf-8 -*-
"""
 Fonctions get_table_name
"""

from typing import Dict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_etude_parameters(moteur: str, periodicite: str, periode: str, logger: 'LOGGER' = None) -> Dict[str, str]:
    """Construction du dictionnaire d'etude parameters

    :param moteur: valeur de la clé 'Moteur'
    :param periodicite: valeur de la clé 'Periodicite'
    :param periode: valeur de la clé 'Periode'
    :param logger: gestionnaire des logs
    :return: dict etude_parameters
    """
    try:
        return dict(Moteur=moteur, Periodicite=periodicite, Periode=periode)
    except Exception as e:
        logger.exception(e)
