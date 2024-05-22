# -*- coding: utf-8 -*-
"""
 Get des schema de tables SQL à partir d'un fichier JSON de définition
"""

import os
from typing import List, Tuple
from typing import TYPE_CHECKING

from load_json import load_json
from sql_schema import build_schema
from sql_schema import get_list_data_figees
from time_periodes import get_cle_periode

if TYPE_CHECKING:
    from logger import LOGGER


def get_version_source() -> dict:
    return {'VersionSource':  {'sql_type': 'INT', 'nullable': 'NOT NULL'}}


def get_schema_from_json(path_schema: str, table: str, periodicite: str = None, columns: List[str] = None,
                         format: dict = None, logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:
    """Construction d'un schema SQL pour la table demandée

    :rtype: object
    :param path_schema: path vers le dir contenant la défintion des schema SQL
    :param table: table dont on veut le schema SQL
    :param periodicite: periodicité [Optionel]
    :param columns: list des colonnes auxquelles on veut restreindre le schema SQL [Optionel]
    :param format: paramètres supplémentaires pour construire le schema SQL [Optionel]
    :param logger: gestionnaire de slogs [Optionel]
    :return: Schema sql
    """
    json_schema = dict()

    tables_locales = ['banks','salaries']

    tables_version_source = ['univers', 'paneliste', 'referentiel_presentations', 'achats', 'ventes','sog', 'sox4']

    tables_rfsotc = ['rfsotc', 'rfind', 'rfeta', 'repartjurephmra']

    niveaux = ['uga', 'departement', 'france']
    travelling_uga = ['travelling_uga_' + niveau for niveau in niveaux]
    repart_prescripteur = ['repart_prescripteur_' + niveau for niveau in niveaux]
    repart_prescripteur_hopital = ['repart_prescripteur_hopital_' + niveau for niveau in niveaux]
    repart_pharmacie = ['repart_pharmacie_' + niveau for niveau in niveaux]
    repart_pharmacie_hopital = ['repart_pharmacie_hopital_' + niveau for niveau in niveaux]
    travelling_etablissement = ['travelling_etablissement_' + niveau for niveau in ['presentation', 'uga']]
    travelling_produit_uga = ['travelling_uga_produit_' + niveau for niveau in niveaux]
    repart_prescripteur_produit = ['repart_prescripteur_produit_' + niveau for niveau in niveaux]
    repart_prescripteur_hopital_produit = ['repart_prescripteur_hopital_produit_' + niveau for niveau in niveaux]
    repart_pharmacie_produit = ['repart_pharmacie_produit_' + niveau for niveau in niveaux]
    repart_pharmacie_hopital_produit = ['repart_pharmacie_hopital_produit_' + niveau for niveau in niveaux]
    travelling_etablissement_produit = ['travelling_etablissement_produit_' + niveau for niveau in ['presentation']]

    tables_travelling = list()
    tables_travelling.extend(travelling_uga)
    tables_travelling.extend(repart_prescripteur)
    tables_travelling.extend(repart_prescripteur_hopital)
    tables_travelling.extend(repart_pharmacie)
    tables_travelling.extend(repart_pharmacie_hopital)
    tables_travelling.extend(travelling_etablissement)
    tables_travelling.extend(travelling_produit_uga)
    tables_travelling.extend(repart_prescripteur_produit)
    tables_travelling.extend(repart_prescripteur_hopital_produit)
    tables_travelling.extend(repart_pharmacie_produit)
    tables_travelling.extend(repart_pharmacie_hopital_produit)
    tables_travelling.extend(travelling_etablissement_produit)

    origin_travelling_uga = ['orihebu6', 'orihebu7', 'origin6', 'origin7', 'origin8']
    origin_repart_prescripteur = ['orihebs6', 'orihebs7', 'origins6', 'origins7', 'origins8']
    origin_repart_prescripteur_hopital = ['orihebhs6', 'orihebhs7', 'originhs6', 'originhs7', 'originhs8']
    origin_repart_pharmacie = ['sogsheb2', 'sogs2', 'sogs4']
    origin_repart_pharmacie_hopital = ['sogshopheb2', 'sogshop2', 'sogshop4']
    origin_travelling_etablissement = ['orihebh6', 'orihebh7', 'originh6', 'originh7', 'originh8']

    tables_origin = list()
    tables_origin.extend(origin_travelling_uga)
    tables_origin.extend(origin_repart_prescripteur)
    tables_origin.extend(origin_repart_prescripteur_hopital)
    tables_origin.extend(origin_repart_pharmacie)
    tables_origin.extend(origin_repart_pharmacie_hopital)
    tables_origin.extend(origin_travelling_etablissement)

    tables_figees = get_list_data_figees('data_figees')

    tables_sox = ['soxhebdo', 'sog', 'sox4', 'soxseg2', 'soxhcol_national', 'soxhcol', 'soxcol', 'poids',
                  'poids_jumeaux']

    tables_stocks = ['memosf', 'stocks', 'stocks_extrapoles', 'stockx']

    tables_moteurs = ['univers', 'paneliste', 'referentiel_presentations', 'achats', 'ventes', 'pmgtg', 'obsprix']
    tables_moteurs += ['signorm', 'poidsj', 'sognow', 'pdv_indic']

    tables_indic = ['compomarcheclient', 'compoperiode', 'comporeseau', 'compotype', 'comporemplace']

    tables_pilotage = ['correspondance_stat_gersit', 'correspondance_suivi_production']

    tables_soc = ['annuaire', 'catalogue', 'nouveau_medicament', 'panel', 'repartition_transaction', 'transaction_pan',
                  'soc', 'clonage', 'rang_7']

    tables_calls = ['calls_ventes', 'calls_refus']

    tables_relance = ['relance_gestion', 'relance_globale', 'relance_moteur', 'relance_niveau', 'relance_table',
                      'panier_presentation', 'sognow_global', 'sognow_moteur', 'sognow_table']

    tables_production = ['production_globale', 'production_moteur', 'production_niveau', 'production_table',
                         'depot_sognow']

    tables_production_calls_ventes = ['production_calls_ventes', 'production_calls_ventes_tables',
                                      'production_calls_achats']

    tables_production_indic = ['production_indic']

    if table in tables_rfsotc:
        path_rfsotc = os.path.join(path_schema, 'moteurs_statistique', 'rfsotc', table + '.json')
        json_schema.update(load_json(path_rfsotc, logger=logger))
    elif table in tables_travelling:
        path_travelling = os.path.join(path_schema, 'moteurs_statistique', 'travelling')
        if table in travelling_uga:
            path_travelling = os.path.join(path_travelling, 'travelling_uga.json')
        elif table in repart_prescripteur + repart_prescripteur_hopital:
            path_travelling = os.path.join(path_travelling, 'repart_prescripteur.json')
        elif table in repart_pharmacie + repart_pharmacie_hopital:
            path_travelling = os.path.join(path_travelling, 'repart_pharmacie.json')
        elif table in travelling_etablissement:
            path_travelling = os.path.join(path_travelling, 'travelling_etablissement.json')
        elif table in travelling_produit_uga:
            path_travelling = os.path.join(path_travelling, 'travelling_uga_produit.json')
        elif table in repart_prescripteur_produit + repart_prescripteur_hopital_produit:
            path_travelling = os.path.join(path_travelling, 'repart_prescripteur_produit.json')
        elif table in repart_pharmacie_produit + repart_pharmacie_hopital_produit:
            path_travelling = os.path.join(path_travelling, 'repart_pharmacie_produit.json')
        elif table in travelling_etablissement_produit:
            path_travelling = os.path.join(path_travelling, 'travelling_etablissement_produit.json')
        json_schema.update(load_json(path_travelling, logger=logger))
    elif table in tables_origin:
        path_origin = os.path.join(path_schema, 'moteurs_statistique', 'origin')
        if table in origin_travelling_uga:
            path_origin = os.path.join(path_origin, 'origin_uga.json')
        elif table in origin_travelling_etablissement:
            path_origin = os.path.join(path_origin, 'origin_hopital.json')
        elif table in origin_repart_prescripteur + origin_repart_prescripteur_hopital:
            path_origin = os.path.join(path_origin, 'origin_specialite.json')
        elif table in origin_repart_pharmacie + origin_repart_pharmacie_hopital:
            path_origin = os.path.join(path_origin, 'sogs.json')
        json_schema.update(load_json(path_origin, logger=logger))
    elif table in tables_sox:
        path_sox = os.path.join(path_schema, 'moteurs_statistique', 'sox')
        if table in ['soxhebdo', 'sog', 'sox4']:
            path_sox = os.path.join(path_sox, 'sox.json')
        elif table == 'soxseg2':
            path_sox = os.path.join(path_sox, 'soxseg2.json')
        elif table == 'soxhcol_national':
            path_sox = os.path.join(path_sox, 'soxhcol_national.json')
        else:
            path_sox = os.path.join(path_sox, table + '.json')
        json_schema.update(load_json(path_sox, logger=logger))
    elif table in tables_stocks:
        json_schema.update(load_json(os.path.join(path_schema, 'moteurs_statistique', 'stocks', f'{table}.json'),
                                     logger=logger))
    elif table in tables_soc:
        json_schema.update(load_json(os.path.join(path_schema, 'moteurs_statistique', 'soc', f'{table}.json'),
                                     logger=logger))
    elif table in tables_figees:
        json_schema.update(load_json(os.path.join(path_schema, 'data_figees', f'{table}.json'), logger=logger))
    elif table in tables_moteurs:
        json_schema.update(load_json(os.path.join(path_schema, 'moteurs_statistique', f'{table}.json'), logger=logger))
    elif table in tables_indic:
        json_schema.update(load_json(os.path.join(path_schema, 'indic', f'{table}.json'), logger=logger))
    elif table in tables_pilotage:
        json_schema.update(load_json(os.path.join(path_schema, 'pilotage', f'{table}.json'), logger=logger))
    elif table in tables_calls:
        json_schema.update(load_json(os.path.join(path_schema, 'calls', f'{table}.json'), logger=logger))
    elif table in tables_relance:
        json_schema.update(load_json(os.path.join(path_schema, 'relance', f'{table}.json'), logger=logger))
    elif table in tables_production:
        json_schema.update(load_json(os.path.join(path_schema, 'production', f'{table}.json'), logger=logger))
    elif table in tables_production_calls_ventes:
        json_schema.update(load_json(os.path.join(path_schema, 'production_calls', f'{table}.json'), logger=logger))
    elif table in tables_production_indic:
        json_schema.update(load_json(os.path.join(path_schema, 'production_indic', f'{table}.json'), logger=logger))
    elif table in tables_locales:
        json_schema.update(load_json(os.path.join(path_schema, 'moteurs_locales', f'{table}.json'), logger=logger))

    if table in tables_version_source and periodicite in ['mensuel', 'mensueldebutmois']:
        json_schema.update(get_version_source())

    cle_periode = get_cle_periode(periodicite, logger=logger)

    format = {'ClePeriode': cle_periode} if format is None else {**{'ClePeriode': cle_periode}, **format}

    schema = build_schema(json_schema, format=format, logger=logger)

    if columns is not None:
        schema = list(filter(lambda tp: tp[0] in columns, schema))

    return schema
