# -*- coding: utf-8 -*-
"""
 Initialisation d'une class d'extraction d'historique
"""

from extract_calls_ventes import ExtractCallsVentes
from extract_pmgtg import ExtractPMGTG
from extract_poidsj import ExtractPoidsj
from extract_repartjurephmra import ExtractRepartjurephmra
from extract_rfeta import ExtractRfeta
from extract_rfind import ExtractRfind
from extract_rfsotc import ExtractRfsotc
from extract_signorm import ExtractSignorm
from extract_stocks import ExtractStocks
from extract_travelling import ExtractTravelling
from extract_ventes import ExtractVentes


moteurs_travelling = ['travelling_uga', 'repart_prescripteur', 'repart_pharmacie', 'repart_prescripteur_hopital',
                      'repart_pharmacie_hopital', 'travelling_etablissement']


def get_extracteur(parameters: dict):
    if parameters['Moteur'] in moteurs_travelling:
        return ExtractTravelling(parameters)
    elif parameters['Moteur'] == 'rfsotc':
        if parameters['Table'] == 'rfind':
            return ExtractRfind(parameters)
        elif parameters['Table'] == 'rfeta':
            return ExtractRfeta(parameters)
        elif parameters['Table'] == 'rfsotc':
            return ExtractRfsotc(parameters)
        elif parameters['Table'] == 'repartjurephmra':
            return ExtractRepartjurephmra(parameters)
    elif parameters['Moteur'] == 'calls':
        if parameters['Table'] == 'calls_ventes':
            return ExtractCallsVentes()
    elif parameters['Moteur'] == 'pmgtg':
        return ExtractPMGTG(parameters)
    elif parameters['Moteur'] == 'stocks':
        return ExtractStocks(parameters)
    elif parameters['Moteur'] == 'signorm':
        return ExtractSignorm(parameters)
    elif parameters['Moteur'] == 'poidsj':
        return ExtractPoidsj(parameters)
    elif parameters['Moteur'] == 'ventes':
        return ExtractVentes(parameters)
