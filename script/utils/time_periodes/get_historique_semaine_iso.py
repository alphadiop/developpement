# -*- coding: utf-8 -*-
"""
 Récupération d'une historique à partir d'un numéro de semaine iso
"""

import datetime
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def get_historique_semaine_iso(cle_semaine_iso: str, historique: int, logger: 'LOGGER' = None) -> List[str]:
    """
    Nombre de semaine d'historique à partir de cle_semaine_iso

    :param cle_semaine_iso: numnéro de semaine iso pour lequel l'historique est calculé
    :param historique: nombre de semaine d'historique souhaité
    :param logger: gestion des logs
    :return: list de semaine iso
    """
    try:
        iso_semaine = datetime.datetime.strptime(cle_semaine_iso + '0', '%Y%U%w')
        list_semaine_iso = [cle_semaine_iso]
        for dt in range(0, historique):
            iso_calendar = (iso_semaine + datetime.timedelta(days=-7*dt)).isocalendar()
            list_semaine_iso.append(str(iso_calendar[0]) + str(iso_calendar[1]).zfill(2))
        return sorted(list((set(list_semaine_iso))), reverse=True)[:historique]
    except Exception as e:
        logger.exception(e)
