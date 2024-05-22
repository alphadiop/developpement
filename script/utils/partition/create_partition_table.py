# -*- coding: utf-8 -*-
"""
  Création de partition sur les tables moteur stat
"""

from typing import Dict, List

from partition import get_path_partition
from partition.gestion_partition_table import GestionPartitionTable


class CreatePartitionTable(GestionPartitionTable):

    def __init__(self, parameters: Dict[str, str]):
        GestionPartitionTable.__init__(self, parameters)

    def run(self):
        self.create_clustered_index()
        self.drop_scheme_function_partition()
        file_groups = self.define_file_groups()
        self.create_partition_function(self.periodes, file_groups)
        self.create_partition_scheme(file_groups)
        self.create_clustered_index_partition()
        self.create_cluster_columnstore_partition()
        self.logger.close()

    def create_partition_function(self, periodes: List[str], file_groups: List[str]):
        self.logger.info(f"Création des fonctions de partition {self.name_function}")
        self.sql_operations.create_partition_function(self.name_function, periodes)
        self.sql_operations.alter_database_add_filegroups('STAT', file_groups)
        paths_partition = {key: get_path_partition(self.variable_environnement, key, self.name_table)
                           for key in ['local', 'partage']}
        self.sql_operations.alter_database_add_files('STAT', paths_partition, file_groups)

    def create_partition_scheme(self, file_groups: List[str]):
        self.logger.info(f"Création du schéma de partition {self.name_scheme}")
        self.logger.info(f"FileGroups: {str(file_groups)}")
        self.sql_operations.create_partition_scheme(self.name_scheme, self.name_function, file_groups)


if __name__ == '__main__':
    periodicite = 'hebdo'
    moteur = 'travelling'
    table = 'repart_pharmacie_hopital_produit_uga'
