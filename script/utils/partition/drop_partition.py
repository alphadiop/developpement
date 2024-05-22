# -*- coding: utf-8 -*-
"""
 Drop partition table
"""
from typing import Dict

from partition import get_path_partition
from partition.gestion_partition_table import GestionPartitionTable
from rmtree import rmtree


class DropPartition(GestionPartitionTable):

    def __init__(self, parameters: Dict[str, str]):
        GestionPartitionTable.__init__(self, parameters)

    def run(self):
        self.drop_index()
        self.create_clustered_index()
        self.drop_partition_scheme()
        self.drop_partition_function()
        self.remove_files()
        self.drop_index()
        self.create_cluster_columnstore_partition()
        self.remove_directory_partition()
        self.logger.shutdown()
        self.logger.rename_path_log('OK')

    def drop_partition_scheme(self) -> None:
        self.logger.info(f"Drop de la partition schema '{self.name_scheme}'")
        self.sql_operations.drop_partition_scheme(self.name_scheme)

    def drop_partition_function(self) -> None:
        self.logger.info(f"Drop partition function '{self.name_function}'")
        self.sql_operations.drop_partition_function(self.name_function)

    def remove_files(self) -> None:
        self.logger.info('Remove des files existants')
        file_groups = self.define_file_groups()
        self.sql_operations.alter_database_remove_files('STAT', file_groups)

    def remove_directory_partition(self) -> None:
        path_partition = get_path_partition(self.variable_environnement, 'partage', self.name_table)
        self.logger.info(f"Remove du répertoire de partition: {path_partition}")
        rmtree(path_partition, logger=self.logger)


