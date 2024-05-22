# -*- coding: utf-8 -*-
"""
 Fonction get_moteur_stat
"""

from achats import Achats
from obsprix import OBSPRIX
from origin import Origin
from pdv_indic import PdvIndic
from pdv_prio import PdvPrio
from pilotage import load_moteurs_stat
from pmgtg import PMGTG
from poidsj import POIDSJ
from referentiel_presentations import ReferentielPresentations
from rfsotc import RFSOTC
from sig_relocalise import SigRelocalise
from signorm import SIGNORM
from soc import SOC
from sog import SOG
from sognow import SOGNOW
from sox import SOX
from stocks import Stocks
from stocks_extrapoles import StockExtrapoles
from stockx import Stockx
from travelling import TRAVELLING
from univers_paneliste import UniversPaneliste
from variable_environnement import load_variable_environnement
from ventes import Ventes


def get_moteur_stat(parameters: dict):
    """Get d'une class moteur statistique

    :param parameters: dictionnaire de paramètres
    :return: Class moteur statistique
    """
    variable_environnement = load_variable_environnement()
    moteurs_stat = load_moteurs_stat(variable_environnement)
    moteurs_origin = moteurs_stat.query("Source == 'origin'").Moteur.drop_duplicates().tolist()
    moteurs_travelling = moteurs_stat.query("Source == 'travelling'").Moteur.drop_duplicates().tolist()
    moteur = parameters['Moteur']

    if moteur == 'univers_paneliste':
        return UniversPaneliste(parameters)
    elif moteur == 'referentiel_presentations':
        return ReferentielPresentations(parameters)
    elif moteur == 'achats':
        return Achats(parameters)
    elif moteur == 'stocks':
        return Stocks(parameters)
    elif moteur == 'stockx':
        return Stockx(parameters)
    elif moteur == 'ventes':
        return Ventes(parameters)
    elif moteur == 'pmgtg':
        return PMGTG(parameters)
    elif moteur == 'poidsj':
        return POIDSJ(parameters)
    elif moteur == 'sognow':
        return SOGNOW(parameters)
    elif moteur == 'signorm':
        return SIGNORM(parameters)
    elif moteur == 'rfsotc':
        return RFSOTC(parameters)
    elif moteur in moteurs_origin:
        return Origin(parameters)
    elif moteur == 'obsprix':
        return OBSPRIX(parameters)
    elif moteur in 'sox':
        return SOX(parameters)
    elif moteur == 'soc':
        return SOC(parameters)
    elif moteur in 'sog':
        return SOG(parameters)
    elif moteur == 'pdv_prio':
        return PdvPrio(parameters)
    elif moteur == 'pdv_indic':
        return PdvIndic(parameters)
    elif moteur in moteurs_travelling:
        return TRAVELLING(parameters)
    elif moteur == 'stocks_extrapoles':
        return StockExtrapoles(parameters)
    elif moteur == 'sig_relocalise':
        return SigRelocalise(parameters)
