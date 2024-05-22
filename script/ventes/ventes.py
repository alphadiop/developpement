# -*- coding: utf-8 -*-
import os
import platform
from pathlib import Path
from typing import Dict
import rpy2
import pandas as pd
from requirements import sql_requirements
from moteur_statistique import MoteurStatistique
from sql_schema import get_list_data_figees
from sql_schema import get_columns_from_schema
from sql_schema import get_columns_cast_from_schema
from tabulate_dataframe import tabulate_dataframe
from variable_environnement import get_variable_environnement
from get_path_from_json import get_path_from_json
from sqlalchemy import text
class Ventes(MoteurStatistique):

    def __init__(self, etude_parameters: Dict[str, str]):
        MoteurStatistique.__init__(self, etude_parameters,os.path.dirname(__file__))


    def run(self):
        self.logger.info('='*121)
        #self.chargement_data()
        #self.cheick_version()
        #self.liste_data_base()
        #self.create_table()





    def cheick_version(self):
        version = sql_requirements(self.variable_environnement)
        # path_home = os.environ["PATH"]
        os.add_dll_directory(r"path_to_R/bin/x64/")  # E.g., "C:/Program Files/R/R-4.3.1/bin/x64"
        from rpy2.robjects.packages import importr
        platform = platform.system()
        # ##self.logger.info(f" time of last modification of {path} : {self.convert(os.path.getmtime(path))}")
        print(f"version : {version}")
        # import os
        # os.environ["R_HOME"] = r"D:\Install\R\R-3.6.1"
        # os.environ["PATH"] = r"D:\Install\R\R-3.6.1\bin\x64" + ";" + os.environ["PATH"]
        # import rpy2
        # from rpy2.robjects import pandas2ri, packages
        # pandas2ri.activate()
        # stats = packages.importr('stats')
        #print(f"version : {path_home}")



    @MoteurStatistique.log_this
    def liste_data_base(self):
        query = "select name FROM sys.databases;"
        query = "SELECT * FROM sys.schemas"
        df = self.sql_operations.load_df(query)
        print(f"df : {tabulate_dataframe(df.head())}")

#from sqlalchemy import text

    @MoteurStatistique.log_this
    def chargement_data(self):
        schema = self.get_schema_from_json(table='salaries',periodicite='hebdo')
        table_name = self.get_table_name(table='salaries', periodicite='hebdo')
        self.sql_operations.create_table(table_name,schema,drop_table=True)



    @MoteurStatistique.log_this
    def test_mathode(self):
        self.get_path_test()
        self.lecture_fichier_sql()
        self.afficher_table()
        self.cheick_table()
        self.adiop_get_schema_from_json(table='weather',periodicite='hebdo')


    def get_path_test(self):
        self.logger.info(f"etude_parameters : {self.etude_parameters}")
        self.logger.info(f"etude_parameters of sql : {self.path_parameters['sql']}")
        self.logger.info(f"get_path_sql : {self.get_path_sql(os.path.dirname(__file__))}")
        self.logger.info(f"dict json_data : {self.json_data}")
        self.logger.info(f"path from json_data : {self.json_data['liste_table']}")
        #self.logger.info(f"get_path_from_jsons: {self.get_path_from_jsons()}")

    @MoteurStatistique.log_this
    def afficher_table(self):
        schema = self.get_schema_from_json(table='salaries', periodicite='hebdo')
        column = get_columns_from_schema(schema, logger=self.logger)
        table = self.get_table_name(table='basquet',periodicite='hebdo')
        table = self.get_table_name(table='banks', periodicite='hebdo')
        table = self.get_table_name(table='salaries', periodicite='hebdo')
        df = self.sql_operations.select_top(src_table='[Menage].[dbo].[banks]',nrows=4)
        print(f"df : {tabulate_dataframe(df.head())}")


    def cheick_table(self):
        """ methode mecanique : je defini le chemin de la requete """
        path_query = Path(os.path.join(self.path_parameters['sql'],"sql_files","liste_table","liste_table.sql"))
        with open(path_query, 'r') as query:
            df = pd.read_sql_query(query.read(), self.sql_operations.connexion)
        print(f"df : {tabulate_dataframe(df)}")


    def lecture_fichier_sql(self):
        """ methode mecanique : je defini le chemin de la requete """
        query = self.read_query(query="liste_table",format=dict())
        df = self.sql_operations.load_df(query)
        print(f"df : {tabulate_dataframe(df)}")


    def get_path_query(self,query):
        return get_path_from_json(self.path_parameters['sql'],self.json_data,query, self.logger)


        #query = pd.read_sql_query(path_query,conn)
        #print(query)
        #liste_table = self.sql_operations.load_df("liste_table")
        #print(tabulate_dataframe(liste_table))


    def get_list_data_figees(self):
        return get_list_data_figees(variable='data_figees', logger=self.logger)


if __name__=="__main__":
    parametres = {"Moteur":"ventes","Periodicite":'hebdo','Periode':'202323'}
    Ventes(parametres).run()