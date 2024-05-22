https://sql.sh/https://sql.sh/
Server=localhost\SQLEXPRESS01
create a new table and append data frame values to this table


with engine.connect() as conn:
    conn.execute(sql)
    df = pd.read_csv(r"D:\data\base\data.txt")
    df.to_sql(name='test', con = engine, if_exists ='append', index = False, chunksize = 1000)
conn.close()


****************************************************************************************************************************
import sqlalchemy as db
import urllib
import pandas as pd

server = 'localhost\SQLEXPRESS'
database ='message'
username = 'alphadiop'
password = 'Ibrahima1'
driver = '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 13 for SQL Server};' +
                                  ('SERVER={server},{port};' +
                                   'DATABASE={database};' +
                                   'UID={username};' +
                                   'PWD={password};'
                                   'MARS_Connection=Yes').format(server=server,
                                                                 port=port,
                                                                 database=database,
                                                                 username=username,
                                                                 password=password))
engine = db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
connexion = engine.connect()
 
dim_uga = pd.read_sql('SELECT * FROM tablesnames, engine)
connexion.execute(query)
connexion.close()