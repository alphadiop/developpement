# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path
from typing import List, Tuple
from typing import TYPE_CHECKING

import pandas as pd
import pytest
import sqlalchemy as sql
from tabulate_dataframe import tabulate_dataframe
from logger import LOGGER
from sql_connexion import get_sql_operations
from variable_environnement import get_variable_environnement
from variable_environnement import load_variable_environnement
from write_xml import write_xml

if TYPE_CHECKING:
    from sql_operations import SQLOperations

class SQLquery:
    variable_environnement = load_variable_environnement()
    #print(tabulate_dataframe(variable_environnement))
    def __init__(self,table:str,logger: LOGGER = None):
        self.table = table
        self.logger = logger
        self.start_time, self.total_time = time.time(), None
        self.sql_operations:'SQLOperations' = get_sql_operations()


    def run(self):
        print('')
        self.afficher_table()


    def afficher_table(self):
        query = "SELECT * FROM {0}".format(self.table)
        df = self.sql_operations.load_df(query)
        count = self.sql_operations.count_table(self.table)
        print(f"shape : {count} \n {tabulate_dataframe(df)}")

    # def get_sql_operations(self) -> 'SQLOperations':
    #     odbc_driver = get_variable_environnement(self.variable_environnement, variable='odbc_driver', logger=self.logger)
    #     return get_sql_operations(server_name='dw_gersit',odbc_driver=odbc_driver,connect_args={'autocommit': True},logger=self.logger)



if __name__=="__main__":
    table_sql = '[message].[dbo].[test]'
    SQLquery(table_sql).run()
