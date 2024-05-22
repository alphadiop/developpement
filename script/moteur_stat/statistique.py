# -*- coding: utf-8 -*-
import datetime
import os
import time
from typing import TYPE_CHECKING, Dict, Tuple, List

from load_json import load_json
from moteurs_stat import get_version_source, get_table_name
from sql_connexion import get_sql_operations
from pilotage import load_moteurs_stat
from sql_query import read_query, read_queries
from sql_schema import get_schema_from_json
from sql_schema import adiop_get_schema_from_json
from time_periodes.get_range_date import get_range_date
from variable_environnement import load_variable_environnement
from variable_environnement import get_variable_environnement
from sql_operations import SQLOperations

if TYPE_CHECKING:
    from logger import LOGGER
class STATISTIQUE:
    variable_environnement = load_variable_environnement()
    moteurs_stat = load_moteurs_stat(variable_environnement)

    def __init__(self,path_script:str,path_json:str,logger:'LOGGER') -> None:
        self.path_script:'str' = path_script
        self.logger:'LOGGER'= logger

        self.start_time, self.total_time = time.time(), None
        self.path_parameters : dict = self.get_path_parameters(path_script, path_json)
        self.sql_operations: 'SQLOperations' = self.get_sql_operations()


    def __str__(self) -> str:
        s = 'Path script : {0}'.format(self.path_script)
        return s

    def run_total(self) -> None:
        try:
            self.logger.write_moteur_properties(self.path_parameters['save'])
            self.logger.write_sql_properties(self.sql_operations.sql_parameters)
            self.create_path_save()
            self.verification_prerequis()
            self.run()
            # --> Close Logger
            self.elapsed_time()
            self.logger.close()
            self.logger.rename_path_log('OK')
            self.sql_operations.close()
        except Exception as e:
            self.sql_operations.close()
            self.logger.exception(e)


    def run(self):
        pass

    def create_path_save(self):
        pass

    def verification_prerequis(self):
        pass


    @staticmethod
    def get_moteur(etude_parameters: Dict[str, str]):
        return etude_parameters['Moteur']


    def get_sql_operations(self) -> 'SQLOperations':
        odbc_driver = get_variable_environnement(self.variable_environnement, 'odbc_driver', logger=self.logger)
        return get_sql_operations('dw_gersit', odbc_driver, connect_args={'autocommit': True}, logger=self.logger)


    def elapsed_time(self) -> None:
        try:
            self.total_time = time.time() - self.start_time
            self.logger.info("=" * 121)
            self.logger.info("    Temps d'exécution: {0} secondes ---".format(int(round(self.total_time, 1))))
            self.logger.info("=" * 121)
        except Exception as e:
            self.logger.exception(e)



    def get_total_time(self) -> float:
        return self.total_time

    @staticmethod
    def convert(seconds):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))



    def get_range_date(self) -> Tuple[str, str]:
        """Appel de la fonction get_range_date pour obtenir le range des dates de la période calculée

        :return: range des date de la période [min(date), max(date)]
        """
        try:
            return get_range_date(self.sql_operations, self.etude_parameters['Periodicite'],
                              self.etude_parameters['Periode'], logger=self.logger)
        except Exception as e:
            self.logger.exception(e)


    def get_path_parameters(self, path_script: str, path_json: str) -> dict:
        path_parameters = dict()
        path_parameters['data'] = self.get_path_data()
        path_parameters['path_dw'] = self.get_path_dw()
        path_parameters['sql'] = self.get_path_sql(path_script)
        path_parameters['log'] = self.get_path_log()
        path_parameters['json'] = path_json
        path_parameters['schema'] = self.get_path_schema()
        return path_parameters


    def get_path_data(self) -> str:
        try:
            return os.path.join(get_variable_environnement(self.variable_environnement,
                                                           variable='data', logger=self.logger))
        except Exception as e:
            self.logger.exception(e)


    @staticmethod
    def get_path_sql(path_script:str) -> str:
        return os.path.join(path_script, 'sql_queries')


    def get_path_dw(self) -> str:
        return os.path.join(get_variable_environnement(self.variable_environnement,
                                                       variable='path_dw', logger=self.logger))


    @classmethod
    def get_path_log(cls):
        return os.path.join(get_variable_environnement(cls.variable_environnement,variable='log'))


    def get_json_data(self):
        """
        Evite de charger le fichier JSON s'il est vide
        """
        path = os.path.join(self.path_script, self.path_parameters['json'])
        self.logger.info(f" time of last modification of {path} : {self.convert(os.path.getmtime(path))}")
        if os.path.getsize(path) > 0:
            return load_json(os.path.join(self.path_script, self.path_parameters['json']), logger=self.logger)


    @classmethod
    def get_path_schema(cls) ->str:
        return os.path.join(get_variable_environnement(cls.variable_environnement, variable='schema'))


    def get_sub_paths(self) -> str:
        pass

    @staticmethod
    def get_path_log_complete(path_log: str, sub_path: str) -> str:
        return os.path.join(path_log, sub_path)


    def get_version_source(self, table: str, periodicite: str):
        return get_version_source(self.moteurs_stat, table, periodicite, logger=self.logger)


    def get_table_name(self, table: str, periodicite: str, is_production: bool = False):
        return get_table_name(self.moteurs_stat, table, periodicite, is_production=is_production, logger=self.logger)


    def get_schema_from_json(self, table: str, periodicite: str = None, columns: List[str] = None, format: dict = None):
        return get_schema_from_json(self.path_parameters['schema'],
                                    table, periodicite, columns=columns, format=format,logger=self.logger)

    def adiop_get_schema_from_json(self, table: str, periodicite: str = None, columns: List[str] = None, format: dict = None):
        return adiop_get_schema_from_json(self.path_parameters['schema'],
                                    table, periodicite, columns=columns, format=format,logger=self.logger)

    def execute_queries(self, query: str, format: dict = None) -> None:
        queries = self.read_queries(query, format)
        self.sql_operations.execute_queries(queries)


    def execute_query(self, query: str, format: dict = None) -> None:
        query = self.read_query(query, format)
        self.sql_operations.execute_query(query)


    def execute_query_openquery(self, query: str, dst_table: str, serveur: str, format: dict = None) -> None:
        query = self.read_query(query, format)
        self.sql_operations.execute_query_openquery(query, dst_table, serveur)


    def read_query(self, query: str, format: dict) -> str:
        if format is None:
            format = dict()
        return read_query(self.path_parameters['sql'], self.json_data, query, format=format)


    def read_queries(self, query: str, format: dict) -> List[str]:
        if format is None:
            format = dict()
        return read_queries(self.path_parameters['sql'], self.json_data, query, format=format)


    @staticmethod
    def log_this(original_function):
        def new_function(self, *args):
            self.logger.info("{0} : {1} - START".format(self.etude_parameters['Moteur'], original_function.__name__).upper())
            before = datetime.datetime.now()
            x = original_function(self, *args)
            after = datetime.datetime.now()
            self.logger.info("{0} : {1} - END - Elapsed Time = {2}".format(self.etude_parameters['Moteur'], original_function.__name__, after - before).upper())
            return x

        return new_function