# -*- coding: utf-8 -*-
"""
 Get de la cle periode de l'etude
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_cle_periode(periodicite: str, logger: 'LOGGER' = None) -> str:
    """Get de la cle periode en adéquation avec celle utilisée dans le DW

    :param periodicite: QUOTIDIEN, HEBDO, MENSUUEL or MENSUELDEBUTMOIS
    :param logger: gestionnaire de log
    :return: CleDate, CleSemaineISOAnneeStatistique or CleMoisAnnee
    """
    try:
        if periodicite == 'quotidien':
            return "CleDate"
        elif periodicite == "hebdo":
            return "CleSemaineISOAnneeStatistique"
        elif (periodicite == 'mensuel') or (periodicite == 'mensueldebutmois'):
            return "CleMoisAnnee"
        else:
            return ''
    except Exception as e:
        logger.exception(e)
