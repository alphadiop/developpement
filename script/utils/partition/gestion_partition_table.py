# -*- coding: utf-8 -*-
"""
  Drop de partition sur les tables moteur stat
"""

import os
from typing import Dict, List, Tuple
from typing import TYPE_CHECKING

from get_logger import get_logger
from moteurs_stat import get_table_name
from partition import define_file_groups
from partition.distinct_range import distinct_range
from partition.get_attributs import get_attribut_partition
from pilotage import load_moteur_stat
from sql_connexion import get_sql_operations
from time_periodes import get_cle_periode
from variable_environnement import load_variable_environnement, get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER
    from typing import Dict


class GestionPartitionTable:
    variable_environnement = load_variable_environnement()

    def __init__(self, parameters: Dict[str, str]):
        self.parameters = parameters
        self.logger = self.get_logger()
        self.table_dw = self.get_table_dw()

        self.sql_operations = get_sql_operations(connect_args={'autocommit': True}, logger=self.logger)
        self.cle_periode = get_cle_periode(self.parameters['Periodicite'], logger=self.logger)
        self.periodes = self.get_periodes()
        self.moteurs_stat = load_moteur_stat(self.variable_environnement, self.parameters['Periodicite'], logger=self.logger)

        self.name_table, self.name_function, self.name_scheme, self.name_index = self.get_attribut_partition()

    def get_logger(self) -> 'LOGGER':
        path_log = os.path.join(get_variable_environnement(self.variable_environnement, 'log'), 'partition',
                                self.parameters['Table'], self.parameters['Periodicite'])
        return get_logger({'Moteur': self.parameters['Moteur'], 'Periodicite': self.parameters['Periodicite']}, path_log)

    def get_table_dw(self):
        moteurs_stat = load_moteur_stat(self.variable_environnement, self.parameters['Periodicite'])
        return get_table_name(moteurs_stat, self.parameters['Table'], self.parameters['Periodicite'],
                              is_production=True)

    def get_attribut_partition(self) -> Tuple[str, str, str, str]:
        name_table, name_function, name_scheme, name_index = get_attribut_partition(self.table_dw)
        self.logger.info(f'Table Name: {name_table}')
        self.logger.info(f'Partition Function: {name_function}')
        self.logger.info(f'Partition Scheme: {name_scheme}')
        self.logger.info(f'Table DW: {self.table_dw}')
        self.logger.info(f'Table Index: {name_index}')

        return name_table, name_function, name_scheme, name_index

    def get_periodes(self) -> List[str]:
        periodes = distinct_range(self.sql_operations, self.table_dw, self.cle_periode)
        self.logger.info(f"Periodes disinctes sur la table {self.table_dw}: \n {', '.join(periodes)}")
        return periodes

    def create_clustered_index(self) -> None:
        self.logger.info(f"Création d'un clustered index sur la table '{self.table_dw}'")
        self.sql_operations.drop_index(self.table_dw, self.name_index)
        self.sql_operations.create_clustered_index(self.table_dw, self.name_index, [(self.cle_periode, '')])

    def drop_scheme_function_partition(self) -> None:
        self.logger.info(f"Drop des schéma et function de partition sur l'ensemble des périodes: {self.name_scheme} "
                         f"et {self.name_function}")
        self.sql_operations.drop_partition_scheme(self.name_scheme)
        self.sql_operations.drop_partition_function(self.name_function)

    def create_clustered_index_partition(self):
        self.logger.info(f"Création d'un clustered index '{self.name_index}'"
                         f" basé sur le schéma de partition '{self.name_scheme}'")
        self.sql_operations.create_clustered_index(self.table_dw, self.name_index,
                                              [(self.cle_periode, '')], on=f'[{self.name_scheme}]({self.cle_periode})',
                                              options=['PAD_INDEX = OFF', 'STATISTICS_NORECOMPUTE = OFF',
                                                       'SORT_IN_TEMPDB = OFF',
                                                       'DROP_EXISTING = ON', 'ONLINE = OFF', 'ALLOW_ROW_LOCKS = OFF',
                                                       'ALLOW_PAGE_LOCKS = OFF'])

    def create_cluster_columnstore_partition(self):
        self.logger.info(f"Création d'un index columnstore pour prendre en compte "
                         f"le schéma de partition '{self.name_scheme}'")
        self.sql_operations.create_clustered_columnstore_index(self.table_dw, self.name_index,
                                                               options=['DROP_EXISTING = ON'], partition=None)

    def drop_index(self):
        self.logger.info(f"Drop index: {self.table_dw}, {self.name_index}")
        self.sql_operations.drop_index(self.table_dw, self.name_index)

    def define_file_groups(self) -> List[str]:
        return define_file_groups(self.name_table, self.periodes, logger=self.logger)
