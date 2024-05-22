# -*- coding: utf-8 -*-
"""
 Definition des conditions de jointure pour le Mode de Relance
"""

import os
from typing import Dict
from typing import TYPE_CHECKING

#from path import Path
from pathlib import Path

from load_json import load_json
from moteurs_stat.get_table_name import get_table_name

if TYPE_CHECKING:
    from pandas import DataFrame

relance_join = load_json(os.path.join(Path(os.path.dirname(__file__)), r'json_data\relance_join.json'))


def get_join_relance(moteur: str,  periodicite: str, moteurs_stat: 'DataFrame') -> Dict[str, str]:
    """Definition de la condition de jointure avec le panier présentation pour les mode de relance

    :param moteur: nom du moteur dont on calcul un mode de relance
    :param periodicite: périodicité du moteur caluclé
    :param moteurs_stat: tables des propriétés des moteurs_locales
    :return: dictionnaire des conditions de jointure des tables du moteurs_locales calculé
    """
    query = "INNER JOIN #panier_presentation ON #panier_presentation.{0} = "
    query = {'presentation': query.format('ClePresentation'),
             'produit': query.format('Produit')}
    join = dict()
    for table in relance_join[moteur]:
        src = get_table_name(moteurs_stat, table, periodicite)
        if len(src.split('.')) >= 4:
            src_split = map(lambda x: x.replace('[', '').replace(']', ''), src.split('.')[-2:])
            src = '.'.join(src_split)

        if table in ['travelling_uga_uga', 'travelling_uga_departement', 'travelling_uga_france']:
            join.update({table: query['presentation'] + " {0}.ClePresentation".format(src)})
        elif table in ['soxhebdo']:
            join.update({table: {"presentation": "#panier_presentation.ClePresentation <> #DonneesSource.ClePresentation",
                                 "produit": "#panier_presentation.Produit <> #DonneesSource.Produit"}})
        elif table in ['travelling_uga_produit_uga', 'travelling_uga_produit_departement',
                       'travelling_uga_produit_france']:
            join.update({table: query['produit'] + " {0}.Produit".format(src)})
    return join





    # query = "INNER JOIN #Panier ON #Panier.ClePresentation = "
    # if self.get_moteur(self.etude_parameters) == 'achats':
    #     return query + " [FaitJourAchat].ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'ventes':
    #     return query + " [FaitLigneFactureSO].ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'sox':
    #     table_ventes = self.get_table_name('ventes', periodicite)
    #     return query + " {0}.ClePresentationCollecte".format(table_ventes)
    # elif self.get_moteur(self.etude_parameters) == 'poidsj':
    #     return query + " {TableVentes}.ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'sognow':
    #     return query + " {TablePoidsj}.ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'signorm':
    #     return query + "  {TableAchats}.ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'soc':
    #     return query + "  [FaitMoisFactureSO].ClePresentationCollecte"
    # elif self.get_moteur(self.etude_parameters) == 'rfsotc':
    #     return query + " [FaitLigneFactureSO].ClePresentation"
    # elif self.get_moteur(self.etude_parameters) in moteurs_origin:
    #     join_command = dict()
    #
    #     if self.get_moteur(self.etude_parameters) in ['orihebu6', 'sogsheb2', 'sogshebhop2']:
    #         soxhebdo = self.get_table_name('soxhebdo', periodicite)
    #         join_command.update({'soxhebdo': query + " {0}.ClePresentation".format(soxhebdo)})
    #     elif self.get_moteur(self.etude_parameters) in ['origin6', 'sogs2', 'sogshop2']:
    #         sog = self.get_table_name('sog', periodicite)
    #         join_command.update({'sog': query + " {0}.ClePresentation".format(sog)})
    #     elif self.get_moteur(self.etude_parameters) in ['origin8', 'sogs4', 'sogshop4']:
    #         sox4 = self.get_table_name('sox4', periodicite)
    #         join_command.update({'sox4': query + " {0}.ClePresentation".format(sox4)})
    #     elif self.get_moteur(self.etude_parameters) in ['orihebh6', 'orihebs6', 'orihebhs6']:
    #         orihebu6 = self.get_table_name('orihebu6', periodicite)
    #         join_command.update({'orihebu6': query + " {0}.ClePresentation".format(orihebu6)})
    #     elif self.get_moteur(self.etude_parameters) in ['orihebh7', 'orihebs7', 'orihebhs7']:
    #         orihebu7 = self.get_table_name('orihebu7', periodicite)
    #         join_command.update({'orihebu7': query + " {0}.ClePresentation".format(orihebu7)})
    #     elif self.get_moteur(self.etude_parameters) in ['originh6', 'origins6', 'originhs6']:
    #         origin6 = self.get_table_name('origin6', periodicite)
    #         join_command.update({'origin6': query + " {0}.ClePresentation".format(origin6)})
    #     elif self.get_moteur(self.etude_parameters) in ['originh7', 'origins7', 'originhs7']:
    #         origin7 = self.get_table_name('origin7', periodicite)
    #         join_command.update({'origin7': query + " {0}.ClePresentation".format(origin7)})
    #     elif self.get_moteur(self.etude_parameters) in ['originh8', 'origins8', 'originhs8']:
    #         origin8 = self.get_table_name('origin8', periodicite)
    #         join_command.update({'origin8': query + " {0}.ClePresentation".format(origin8)})
    #
    #     if self.get_moteur(self.etude_parameters) in ["orihebu6", "orihebu7", "origin6", "origin7", "origin8"]:
    #         travelling_uga_uga = self.get_table_name('travelling_uga_uga', periodicite)
    #         travelling_uga_departement = self.get_table_name('travelling_uga_departement', periodicite)
    #         travelling_uga_france = self.get_table_name('travelling_uga_france', periodicite)
    #         join_command.update({
    #             'travelling_uga_uga': query + " {0}.ClePresentation".format(travelling_uga_uga),
    #             'travelling_uga_departement': query + " {0}.ClePresentation".format(travelling_uga_departement),
    #             'travelling_uga_france': query + " {0}.ClePresentation".format(travelling_uga_france)})
    #     elif self.get_moteur(self.etude_parameters) in ["orihebs6", "orihebs7", "origins6", "origins7", "origins8"]:
    #         repart_prescripteur_uga = self.get_table_name('repart_prescripteur_uga', periodicite)
    #         repart_prescripteur_departement = self.get_table_name('repart_prescripteur_departement', periodicite)
    #         repart_prescripteur_france = self.get_table_name('repart_prescripteur_france', periodicite)
    #         join_command.update({"repart_prescripteur_uga": query + " {0}.ClePresentation".format(repart_prescripteur_uga),
    #                              "repart_prescripteur_departement": query + " {0}.ClePresentation".format(repart_prescripteur_departement),
    #                              "repart_prescripteur_france": query + " {0}.ClePresentation".format(repart_prescripteur_france)})
    #     elif self.get_moteur(self.etude_parameters) in ["orihebhs6", "orihebhs7", "originhs6", "originhs7", "originhs8"]:
    #         repart_prescripteur_hopital_uga = self.get_table_name('repart_prescripteur_hopital_uga', periodicite)
    #         repart_prescripteur_hopital_departement = self.get_table_name('repart_prescripteur_hopital_departement', periodicite)
    #         repart_prescripteur_hopital_france = self.get_table_name('repart_prescripteur_hopital_france', periodicite)
    #         join_command.update({"repart_prescripteur_hopital_uga": query + " {0}.ClePresentation".format(repart_prescripteur_hopital_uga),
    #                              "repart_prescripteur_hopital_departement": query + " {0}.ClePresentation".format(repart_prescripteur_hopital_departement),
    #                              "repart_prescripteur_hopital_france": query + " {0}.ClePresentation".format(repart_prescripteur_hopital_france)})
    #     elif self.get_moteur(self.etude_parameters) in ["sogsheb2", "sogs2", "sogs4"]:
    #         repart_pharmacie_uga = self.get_table_name('repart_pharmacie_uga', periodicite)
    #         repart_pharmacie_departement = self.get_table_name('repart_pharmacie_departement', periodicite)
    #         repart_pharmacie_france = self.get_table_name('repart_pharmacie_france', periodicite)
    #         join_command.update({"repart_pharmacie_uga": query + " {0}.ClePresentation".format(repart_pharmacie_uga),
    #                              "repart_pharmacie_departement": query + " {0}.ClePresentation".format(repart_pharmacie_departement),
    #                              "repart_pharmacie_france": query + " {0}.ClePresentation".format(repart_pharmacie_france)})
    #     elif self.get_moteur(self.etude_parameters) in ["sogshebhop2", "sogshop2", "sogshop4"]:
    #         repart_pharmacie_hopital_uga = self.get_table_name('repart_pharmacie_hopital_uga', periodicite)
    #         repart_pharmacie_hopital_departement = self.get_table_name('repart_pharmacie_hopital_departement', periodicite)
    #         repart_pharmacie_hopital_france = self.get_table_name('repart_pharmacie_hopital_france', periodicite)
    #         join_command.update({"repart_pharmacie_hopital_uga": query + " {0}.ClePresentation".format(repart_pharmacie_hopital_uga),
    #                              "repart_pharmacie_hopital_departement": query + " {0}.ClePresentation".format(repart_pharmacie_hopital_departement),
    #                              "repart_pharmacie_hopital_france": query + " {0}.ClePresentation".format(repart_pharmacie_hopital_france)})
    #     elif self.get_moteur(self.etude_parameters) in ["orihebh6", "orihebh7", "originh6", "originh7", "originh8"]:
    #         travelling_etablissement_presentation = self.get_table_name('travelling_etablissement_presentation', periodicite)
    #         join_command.update({'travelling_etablissement_presentation': query + " {0}.ClePresentation".format(travelling_etablissement_presentation)})
    #
    #     return join_command
