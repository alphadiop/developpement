# -*- coding: utf-8 -*-
"""
  Drop de partition sur les tables moteur stat
"""

from typing import Dict
from typing import TYPE_CHECKING

from gestion_partition_table import GestionPartitionTable
from partition import get_path_partition, define_file_groups
from rmtree import rmtree

if TYPE_CHECKING:
    pass


class DropPartitionTable(GestionPartitionTable):

    def __init__(self, parameters: Dict[str, str]):
        GestionPartitionTable.__init__(self, parameters)

    def run(self):
        name_table, name_function, name_scheme, name_index = self.get_attribut_partition()
        self.sql_operations.drop_index(self.table_dw, name_index)
        self.create_clustered_index(name_index)
        self.drop_scheme_function_partition(name_scheme, name_function)
        self.remove_files_filegroups(name_table)
        self.create_clustered_columnstore_index(name_table, name_index)
        self.remove_dir_partition(name_table)
        self.logger.close()

    def remove_files_filegroups(self, name_table: str):
        self.logger.info('Remove des file existants')
        file_groups = define_file_groups(name_table, self.periodes)
        self.sql_operations.alter_database_remove_files('STAT', file_groups)

        self.logger.info("Remove des file group existants")
        self.sql_operations.alter_database_remove_filegroups('STAT', file_groups)

    def create_clustered_columnstore_index(self, name_table, name_index):
        self.logger.info(f"Create Clustered Columnstore Index: {name_table}, {name_index}")
        self.sql_operations.create_clustered_columnstore_index(name_table, name_index, options=['DROP_EXISTING = ON'])

    def remove_dir_partition(self, name_table: str):
        path_partition = get_path_partition(self.variable_environnement, 'partage', name_table)
        self.logger.info("Remove du répertoire de partition: {0}".format(path_partition))
        rmtree(path_partition, logger=self.logger)

