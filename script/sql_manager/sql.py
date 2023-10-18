import pyodbc
import numpy as np
from tabulate import tabulate
import pandas as pd

import ast
import urllib
from typing import Dict
from typing import TYPE_CHECKING
import sqlalchemy
import sqlalchemy as db
import urllib
from urllib.parse import quote
from sqlalchemy import create_engine

from variable_environnement.get_variable_environnement import get_variable_environnement
from variable_environnement.load_variable_environnement import load_variable_environnement


# from param_server import load_variable_environnement
# from param_server import get_variable_environnement


class Connexion:

    variable_environnement = load_variable_environnement()

    def __init__(self, server_name: str, odbc_driver: str, connect_args: dict = None, logger: 'LOGGER' = None):
        self.logger = logger
        self.sql_parameters = self.get_sql_parameters(server_name)
        self.engine = self.get_engine(odbc_driver, connect_args)
        self.connexion = self.get_sql_connexion()

    def get_connexion_params(self,odbc_driver):
        try:
            conn_str = ((r'DRIVER={{{{odbc_driver}}}};' +
                        r'SERVER={server};' +
                        r'DATABASE={database};' +
                        r'UID={username};' +
                        r'PWD={password};'
                        r'Trusted_Connection=Yes').format(odbc_driver=odbc_driver,
                                                        server=self.sql_parameters.get('server'),
                                                        database=self.sql_parameters.get('database'),
                                                        username=self.sql_parameters.get('user'),
                                                        password=self.sql_parameters.get('password')))
            params = urllib.parse.quote_plus(conn_str)
            return params
        except Exception as e:
            self.logger.exception(e)

    def get_engine(self, odbc_driver: str, connect_args: dict) -> sqlalchemy.engine.base.Engine:
        try:
            if connect_args is None:
                connect_args = {}
            return db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.get_connexion_params(odbc_driver),
                                    connect_args=connect_args)
        except Exception as e:
            self.logger.exception(e)

    def get_sql_connexion(self) -> sqlalchemy.engine.base.Connection:
        """
        :return:
        """
        try:
            return self.engine.connect()
        except Exception as e:
            self.logger.exception(e)

    def transaction(self):
        try:
            return self.connexion.begin()
        except Exception as e:
            self.logger.exception(e)

    def commit(self, transaction):
        try:
            transaction.commit()
        except Exception as e:
            self.logger.exception(e)

    def get_sql_parameters(self, server: str) -> Dict[str, str]:
        try:
            parameter = get_variable_environnement(self.variable_environnement, server, logger=self.logger)
            #print(parameter)
            sql_cnxn_parameters = ast.literal_eval(parameter)
            return dict(server=sql_cnxn_parameters.get('server'),
                        port=sql_cnxn_parameters.get('port'),
                        database=sql_cnxn_parameters.get('database'),
                        user=sql_cnxn_parameters.get('user'),
                        password=sql_cnxn_parameters.get('password'))
        except Exception as e:
            self.logger.exception(e)

    def close(self):
        self.connexion.close()


if __name__=="__main__":
    server = get_variable_environnement(variable_environnement=load_variable_environnement(),variable='dw_gersit')
    odbc_driver = get_variable_environnement(variable_environnement=load_variable_environnement(), variable='odbc_driver')
    conn = Connexion(server_name='dw_gersit',odbc_driver=odbc_driver)
    #conn.get_sql_parameters('dw_gersit')
    #print(conn.get_tables())

# conn_str = (
#     r"Driver={ODBC Driver 17 for SQL Server};"
#     r"Server=DIOP\SQLEXPRESS;port = 1433"
#     r"Database=Menage;"
#     r"UID=alphadiop;"
#     r"PWD=Ibrahima1;"
#     r"Trusted_Connection=yes;"
# )
# quoted_conn_str = urllib.parse.quote_plus(conn_str)
# engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted_conn_str))
# sqlcmd = """select * from information_schema.tables"""
# df = pd.read_sql(sqlcmd, engine)
#print(tabulate(df, headers='keys', tablefmt='psql'))
#print(df.head())


#re = get_connexion_params('{ODBC Driver 17 for SQL Server}')
#----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#SQL Server
#ODBC Driver 18 for SQL Server

#using windows authentication
# connx = pyodbc.connect(
#     'DRIVER={SQL Server};'
#     'SERVER=DIOP\SQLEXPRESS;'
#     'Database = Menage;'
#     'Trusted_Connection=yes;')
# #query = "SELECT * FROM Menage.dbo.house_data"
# #df = pd.read_sql(query, connx)
# #print(df.shape)
# #-----------------------------------------------------------------------------



# import pyodbc
#
# conn_str = (
#     r"Driver={ODBC Driver 17 for SQL Server};"
#     r"Server=DIOP\SQLEXPRESS;"
#     r"Database=Menage;"
#     r"UID=alphadiop;"
#     r"PWD=Ibrahima1;"
#     r"Trusted_Connection=yes;"
# )
# conn = pyodbc.connect(conn_str)
#df_new = pd.read_sql_table(table_name='Menage.dbo.house_data', schema='public',conn)
#print(df_new)

#sql_query = pd.read_sql_query('SELECT * FROM Menage.dbo.house_data', conn)
#df = pd.DataFrame(sql_query)
#print(tabulate(df, headers='keys', tablefmt='psql'))
#print(type(df))




#ODBC Driver 17 for SQL Server
#sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=Menage;UID=alphadiop;PWD=Ibrahima1;')
#query = "SELECT * FROM Menage.dbo.house_data"
#df = pd.read_sql(query, sql_conn)
#df.head()

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass')
#---------------------------------------------------------------
#cursor = connx.cursor()
#requete = """ SELECT * FROM Menage.dbo.house_data;"""
#cursor.execute(requete)
#for i in cursor:
    #print(i)

#columns = [column[0] for column in cursor.description]
#results = [columns] + [row for row in cursor.fetchall()]

#for result in results:
    #print(result)
#--------------------------------------------

#import MySQLdb

#sql_query = pd.read_sql_query('SELECT * FROM Menage.dbo.house_data', connexion)
#df = pd.DataFrame(sql_query)
#print(df)



# #driver = '{ODBC Driver 17 for SQL Server}'
# driver = '{SQL Server}'
# server ='DIOP\SQLEXPRESS'
# database = 'Menage'
# username = 'alphadiop'
# password = 'Ibrahima1'
# params = urllib.parse.quote_plus(
#     'Driver=%s;' % driver +
#     'Server=%s;' % server +
#     'Database=%s;' % database +
#     'UID=%s;' % username +
#     'PWD={%s};' % password +
#     "Trusted_Connection=yes;" )
#
# conn_str = 'mssql+pyodbc:///?odbc_connect=' + params
# engine = create_engine(conn_str)
# sqlcmd = """ select * from information_schema.tables """
# data = pd.read_sql(sqlcmd, engine)
# print(tabulate(data, headers='keys', tablefmt='psql'))

