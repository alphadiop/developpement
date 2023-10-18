from sqlalchemy import create_engine, text

import ast
from dataclasses import dataclass
from typing import Dict
import urllib
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import sqlalchemy
from variable_environnement.get_variable_environnement import get_variable_environnement
from variable_environnement.load_variable_environnement import load_variable_environnement


class SQLManager:
    variable_environnement = load_variable_environnement()
    def __init__(self, server_name: str, odbc_driver: str, connect_args: dict = None, logger: 'LOGGER' = None):
        self.logger = logger
        self.sql_parameters = self.get_sql_parameters(server_name)
        self.engine = self.get_engine(odbc_driver, connect_args)
        self.connexion = self.get_sql_connexion()




if __name__=="__main__":
    # marche
    import pandas as pd
    from tabulate import tabulate
    import sqlalchemy
    from sqlalchemy.engine import URL
    # driver = '{SQL Server}'
    # #driver = '{SQL Server}'
    # server = 'DIOP\SQLEXPRESS'
    # #server = 'localhost\SQLEXPRESS'
    # database = 'Menage'
    # trusted_connection = 'yes'
    #
    # # pyodbc connection string
    # connection_string = f'DRIVER={driver};SERVER={server};'
    # connection_string += f'DATABASE={database};'
    # connection_string += f'TRUSTED_CONNECTION={trusted_connection}'
    # connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    #
    # """ more code not shown that uses pyodbc without sqlalchemy """
    # engine = sqlalchemy.create_engine(connection_url)
    # print(engine)
    sqlcmd = """ select * from information_schema.tables """
    # df = pd.read_sql(sqlcmd, engine)
    # print(df.head())
    #**********************************************************************************************************************
    #marche
    # from sqlalchemy import create_engine
    # server = 'localhost\SQLEXPRESS'
    # database = 'Menage'
    # username = 'alphadiop'
    # password = 'Ibrahima1'
    # driver = '{SQL Server}'
    # trusted_connection = 'yes'
    # connection_string = f'DRIVER={driver};SERVER={server};'
    # connection_string += f'DATABASE={database};'
    # connection_string += f'TRUSTED_CONNECTION={trusted_connection}'
    # connection_url = URL.create(drivername="mssql+pyodbc", query={"odbc_connect": connection_string})
    # print(f"connection_url : {connection_url}")
    # engine = create_engine(connection_url)
    # df = pd.read_sql(sqlcmd, engine)
    # print(tabulate(df.head(), headers='keys', tablefmt='psql'))
    #***************************************************************************************************************
    # marche
    # import urllib.parse
    # from sqlalchemy import create_engine
    # import sqlalchemy as db
    # from sqlalchemy import text
    # server = 'localhost\SQLEXPRESS'
    # database = 'message'
    # user = 'alphadiop'
    # password = 'Ibrahima1'
    # driver = 'ODBC Driver 17 for SQL Server'
    # conn = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};'
    # conn_str = urllib.parse.quote_plus(conn)
    # engine = db.create_engine(url=f'mssql+pyodbc:///?odbc_connect={conn_str}', fast_executemany=True)
    # query = text('select * from information_schema.tables')
    # #query = text("CREATE TABLE artiste(artiste_id INTEGER NOT NULL PRIMARY KEY,nom VARCHAR )")
    # print(f"query : {query}")
    # conn = engine.connect()
    # conn.begin()
    # conn.execute(query)
    # conn.commit()
    # conn.close()
    # engine.dispose()
    #*****************************************************************************************************
    # server = 'DIOP\SQLEXPRESS'
    # database = 'message'
    # username = 'alphadiop'
    # password = 'Ibrahima1'
    # driver = 'ODBC Driver 17 for SQL Server'
    # trusted_connection = 'yes'
    from sqlalchemy.engine import URL

    # print("Tables in database:")
    # for row in result:
    #     table = row[0]
    #     print("\t" + table)

    # with engine.connect() as conn:
    #     print(conn)
    #     #conn.execute(sql)
    # conn.close()


    # create a new table and append data frame values to this table
    # df = pd.read_csv(r"D:\data\base\data.txt")
    # #print(df.head())
    # df.to_sql(name='test', con = engine, if_exists ='append', index = False, chunksize = 1000)
     #conn.close()


    #from sqlalchemy import text
    #sql = text('select name from penguins')
    #engine.execute(sql)

    # file = open('query.sql')
    # escaped_sql = sqlalchemy.text(file.read())
    # engine.execute(escaped_sql)

    #df = pd.read_sql(sqlcmd, engine)
    #print(tabulate(df.head(), headers='keys', tablefmt='psql'))
    #******************************************************************************************************************
