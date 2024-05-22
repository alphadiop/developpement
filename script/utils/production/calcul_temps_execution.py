# -*- coding: utf-8 -*-
"""
 Fonction calcul_temps_execution: calcul le laps de temps entre deux instants
"""

import datetime


def calcul_temps_execution(lancement: str, conclusion: str) -> str:
    """Calcul du laps de temps entre deux instants

    :param lancement: instant de départ
    :param conclusion: instant de fin
    :return: laps de temps entre les instants 'lancement' et 'conclusion'
    """
    return str(datetime.datetime.strptime(conclusion, "%d/%m/%Y %H:%M:%S") -
               datetime.datetime.strptime(lancement, "%d/%m/%Y %H:%M:%S"))
