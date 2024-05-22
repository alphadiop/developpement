# -*- coding: utf-8 -*-
"""
  Création de table moteur stat ou rel  nce
"""

import os
from typing import Dict, List, Tuple
from typing import TYPE_CHECKING

from get_logger import get_logger
from moteurs_stat import get_table_name
from partition.get_attributs import get_attribut_partition
from pilotage import load_moteur_stat
from sql_connexion import get_sql_operations
from sql_schema import get_schema_from_json
from variable_environnement import load_variable_environnement, get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


class CreateTableMoteurStatistique:
    variable_environnement = load_variable_environnement()

    def __init__(self, parameters: Dict[str, str], is_relance: bool = False):
        self.parameters = parameters
        self.is_relance = is_relance
        self.logger = self.get_logger()
        self.moteurs_stat = load_moteur_stat(self.variable_environnement, self.parameters['Periodicite'],
                                             logger=self.logger)
        self.sql_operations = get_sql_operations(logger=self.logger)

    def run(self):
        table_dw = self.get_table_dw()

        _, _, _, name_index = get_attribut_partition(table_dw)

        schema = self.get_schema()

        self.sql_operations.create_table(table_dw, schema)

        self.sql_operations.create_clustered_columnstore_index(table_dw, name_index)

        self.sql_operations.close()

        self.logger.close()

    def get_logger(self) -> 'LOGGER':
        path_log = get_variable_environnement(self.variable_environnement, 'log')
        path_log = os.path.join(path_log, 'create_table',
                                self.parameters['Moteur'], self.parameters['Table'], self.parameters['Periodicite'])
        return get_logger({'Moteur': self.parameters['Moteur'], 'Periodicite': self.parameters['Periodicite']},
                          path_log)

    def get_table_dw(self):
        is_production, is_relance = True, False
        if self.is_relance:
            is_production, is_relance = False, True

        return get_table_name(self.moteurs_stat, self.parameters['Table'], self.parameters['Periodicite'],
                              is_production=is_production, is_relance=is_relance, logger=self.logger)

    def get_schema(self) -> List[Tuple[str, str, str]]:
        path_schema = get_variable_environnement(self.variable_environnement, 'schema', logger=self.logger)

        schema = get_schema_from_json(path_schema, self.parameters['Table'], self.parameters['Periodicite'],
                                      logger=self.logger)

        if self.is_relance:
            schema.insert(0, ('IdRelance', 'INT', 'NOT NULL'))
            schema.insert(len(schema), ('DataType', 'TINYINT', 'NOT NULL'))

        return schema
