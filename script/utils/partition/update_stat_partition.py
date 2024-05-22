# -*- coding: utf-8 -*-
"""
 Update partition des tables de la base STAT with new ranges
"""
import os
from typing import Dict
from typing import TYPE_CHECKING

from get_logger import get_logger
from partition.update_partition import UpdatePartition
from pilotage import load_moteur_stat
from tabulate_dataframe import tabulate_dataframe
from variable_environnement import load_variable_environnement, get_variable_environnement

if TYPE_CHECKING:
    from pandas import DataFrame
    from logger import LOGGER


class UpdateStatPartition:
    variable_environnement = load_variable_environnement()

    def __init__(self, parameters: Dict[str, str]):
        self.parameters = parameters

        self.logger = self.get_logger()
        self.moteurs_stat = load_moteur_stat(self.variable_environnement, self.parameters['Periodicite'],
                                             logger=self.logger)

    def run(self):
        self.logger.info("Update des tables de la base STAT")
        self.logger.info(f"Periodicite: {self.parameters['Periodicite']}")
        self.update_partitions()
        self.logger.shutdown()
        self.logger.rename_path_log('OK')

    def get_logger(self) -> 'LOGGER':
        path_log = os.path.join(get_variable_environnement(self.variable_environnement, 'log'), 'update_stat_partition',
                                '', self.parameters['Periodicite'])
        return get_logger({'Moteur': 'update_stat_partition', 'Periodicite': self.parameters['Periodicite']}, path_log)

    def moteur_table_base_stat(self) -> 'DataFrame':
        try:
            moteurs_stat = load_moteur_stat(self.variable_environnement, self.parameters['Periodicite'], logger=self.logger) \
                .drop_duplicates(subset='Table_STAT', keep="last")[['Moteur', 'Table', 'Table_STAT']]

            moteurs_stat = moteurs_stat[(moteurs_stat['Table_STAT'] != '') &
                                        (moteurs_stat['Table_STAT'].str.startswith('[STAT]'))][['Moteur', 'Table']]

            self.logger.info(f"Moteur - Table à partiotionner: \n\n{tabulate_dataframe(moteurs_stat)}")

            return moteurs_stat
        except Exception as e:
            self.logger.exception(e)

    def update_partitions(self):
        moteur_table = self.moteur_table_base_stat()

        try:
            for row in moteur_table.iterrows():
                moteur, table = row[1].Moteur, row[1].Table
                parameters = {'Moteur': moteur, 'Table': table, 'Periodicite': self.parameters['Periodicite']}
                self.logger.info(str(parameters))
                UpdatePartition(parameters).run()
        except Exception as e:
            self.logger.exception(e)


if __name__ == '__main__':
    UpdateStatPartition(dict(Periodicite='hebdo')).run()
