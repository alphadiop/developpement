# -*- coding: utf-8 -*-
"""
 Récupération d'une historique à partir d'un numéro de mois
"""

import datetime
from typing import List
from typing import TYPE_CHECKING

from dateutil.relativedelta import relativedelta

if TYPE_CHECKING:
    from logger import LOGGER


def get_historique_mois_iso(cle_mois_annee: str, historique: int, logger: 'LOGGER' = None) -> List[str]:
    """
    Nombre de semaine d'historique à partir de cle_semaine_iso

    :param cle_mois_annee: numnéro de mois iso pour lequel l'historique est calculé
    :param historique: nombre de mois d'historique souhaité
    :param logger: gestion des logs
    :return: list de mois iso
    """
    try:
        iso_mois = datetime.datetime.strptime(cle_mois_annee, '%Y%m')
        list_mois_iso = list()
        for dt in range(0, historique):
            iso_calendar = iso_mois - relativedelta(months=dt)
            list_mois_iso.append(str(iso_calendar.year) + str(iso_calendar.month).zfill(2))
        return list_mois_iso
    except Exception as e:
        logger.exception(e)
