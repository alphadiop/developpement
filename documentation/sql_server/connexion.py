import os.path

import sqlalchemy as db
import urllib
import pandas as pd
from sqlalchemy import create_engine
from tabulate import tabulate

server = 'localhost\SQLEXPRESS'
database = 'message'
username = 'alphadiop'
password = 'Ibrahima1'
port = '1433'
driver = '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 17 for SQL Server};' +
                                 ('SERVER={server};' +
                                  'DATABASE={database};' +
                                  'UID={username};' +
                                  'PWD={password};'
                                  'MARS_Connection=Yes').format(server=server,
                                                                port=port,
                                                                database=database,
                                                                username=username,
                                                                password=password))
engine = db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

if __name__=="__main__":
    print('*'*121)
    # ******************************************************************************************************************
    # sqlcmd = """ select * from information_schema.tables """
    # df = pd.read_sql(sqlcmd, engine)
    # print(tabulate(df.head(), headers='keys', tablefmt='psql'))
    # ******************************************************************************************************************

    # ******************************************************************************************************************
    # with engine.connect() as conn:
    #     path = r"D:\data_figees"
    #     df = pd.read_csv(os.path.join(path,"nba_all_elo.csv"))
    #     df.to_sql(name='basquet_ball', con=engine, if_exists='append', index=False, chunksize=1000)
    # conn.close()
    #*******************************************************************************************************************