# -*- coding: utf-8 -*-
"""
 Update partition table with new ranges
"""


import os
from typing import Dict, List

from load_json import load_json
from partition import define_file_group, get_path_partition, \
    get_attribut_table
from partition.gestion_partition_table import GestionPartitionTable
from sql_query import read_query


class UpdatePartition(GestionPartitionTable):

    def __init__(self, parameters: Dict[str, str]):
        GestionPartitionTable.__init__(self, parameters)

    def run(self):
        new_ranges = self.get_new_partitions()
        if len(new_ranges) > 0:
            self.drop_index()
            self.update_partitions(new_ranges)
            self.create_clustered_index()
            self.create_clustered_index_partition()
            self.create_cluster_columnstore_partition()

    def get_boundary_values(self) -> List[int]:
        path_sql = os.path.join(os.path.dirname(__file__), 'sql_queries')
        json_data = load_json(os.path.join(path_sql, 'partition.json'), logger=self.logger)

        query = read_query(path_sql, json_data, "get_boundary_values", format=dict(SchemeName=self.name_scheme),
                           logger=self.logger)
        return list(map(lambda x: str(x), self.sql_operations.load_df(query)['BoundaryValue'].values))

    def update_partition(self, name_table: str, name_scheme: str, name_base: str, name_function: str, new_range: str) -> None:
        file_group = define_file_group(name_table, str(new_range), logger=self.logger)
        self.sql_operations.alter_database_add_filegroup(name_base, file_group)
        path_partition = get_path_partition(self.sql_operations.variable_environnement, 'local', name_table, logger=self.logger)
        self.sql_operations.alter_database_add_file(name_base, path_partition, file_group)
        self.sql_operations.alter_partition_scheme(name_scheme, file_group)
        self.sql_operations.alter_partition_function(name_function, new_range)

    def get_new_partitions(self):
        self.logger.info(f"Update de la partition de la table: {self.table_dw}")
        name_base, _, _ = get_attribut_table(self.table_dw, logger=self.logger)
        boundary_values = self.get_boundary_values()
        new_ranges = set(self.periodes).difference(boundary_values)
        if len(new_ranges) == 0:
            self.logger.info("Il n'y a pas de nouvelles partitions à ajouter.")
        else:
            self.logger.info(f"Nouvelles partition à ajouter: {str(new_ranges)}")
        return new_ranges

    def update_partitions(self, new_ranges) -> None:
        self.logger.info("Ajout des nouvelles partitions")
        name_base, _, _ = get_attribut_table(self.table_dw, logger=self.logger)
        for new_range in new_ranges:
            self.logger.info(f"   Partition à ajouter: {new_range}")
            self.update_partition(self.name_table, self.name_scheme, name_base, self.name_function, new_range)


if __name__ == '__main__':
    UpdatePartition(dict(Moteur='univers_paneliste', Table='univers', Periodicite='hebdo')).run()
