import ast
from typing import Dict
import urllib
import sqlalchemy as db
import sqlalchemy
from variable_environnement import get_variable_environnement
from variable_environnement import load_variable_environnement


class SQLManager:
    variable_environnement = load_variable_environnement()
    def __init__(self, server_name: str, odbc_driver: str, connect_args: dict = None, logger: 'LOGGER' = None):
        self.logger = logger
        self.sql_parameters = self.get_sql_parameters(server_name)
        self.engine = self.get_engine(odbc_driver, connect_args)
        self.connexion = self.get_sql_connexion()

    def get_connexion_params(self, odbc_driver: str):
        #'SERVER={server},{port};' faut enlever le port en local
        try:
            params = urllib.parse.quote_plus((r'DRIVER={{{odbc_driver}}};' +
                                              'SERVER={server};' +
                                              'DATABASE={database};' +
                                              'UID={username};' +
                                              'PWD={password};'
                                              'Trusted_Connection=Yes').format(odbc_driver=odbc_driver,
                                                                            server=self.sql_parameters.get('server'),
                                                                            port=self.sql_parameters.get('port'),
                                                                            database=self.sql_parameters.get('database'),
                                                                            username=self.sql_parameters.get('user'),
                                                                            password=self.sql_parameters.get('password')))
            return params
        except Exception as e:
            self.logger.exception(e)

    def get_engine(self, odbc_driver: str, connect_args: dict) -> sqlalchemy.engine.base.Engine:
        try:
            if connect_args is None:
                connect_args = {}
            return db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.get_connexion_params(odbc_driver),connect_args=connect_args)
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


#
if __name__=="__main__":
    import pandas as pd
    from tabulate import tabulate
    import urllib.parse
    from sqlalchemy import create_engine
    param = get_variable_environnement(variable_environnement=load_variable_environnement(),variable='dw_gersit')
    odbc_driver = get_variable_environnement(variable_environnement=load_variable_environnement(),variable='odbc_driver')
    server_name = ast.literal_eval(param)
    # print(f"server_name : {param}")
    # print(f"odbc_driver : {odbc_driver}")
    #conn = SQLManager(server_name='dw_gersit', odbc_driver='ODBC Driver 17 for SQL Server')
#
#     # df = pd.read_sql(sqlcmd, engine)
#     # print(tabulate(df.head(), headers='keys', tablefmt='psql'))
#     # *****************Marche***********************************************************

