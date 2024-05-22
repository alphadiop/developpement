from dataclasses import dataclass
from typing import Dict, Any, Iterable
##https://www.linkedin.com/pulse/connecting-sql-database-python-patrick-j-ryan/
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, inspect
import urllib
from tabulate import tabulate


@dataclass(frozen=True)
class ConnectionSettings:
    """Connection Settings."""
    server: str = 'localhost\SQLEXPRESS'
    database: str = 'message'
    username: str = 'alphadiop'
    password: str = 'Ibrahima1'
    driver: str = '{ODBC Driver 17 for SQL Server}'



class AzureDbConnection:
    """
    Azure SQL database connection.
    """
    def __init__(self, conn_settings: ConnectionSettings, echo: bool = False) -> None:
        conn_params = urllib.parse.quote_plus(
            'Driver=%s;' % conn_settings.driver +
            'Server=%s;' % conn_settings.server +
            'Database=%s;' % conn_settings.database +
            'Uid=%s;' % conn_settings.username +
            'Pwd={%s};' % conn_settings.password +
            "Trusted_Connection=yes;"
        )
        conn_string = f'mssql+pyodbc:///?odbc_connect={conn_params}'
        self.db = create_engine(conn_string, echo=echo)


    def __str__(self):
        s = self.conn_params
        return s

    def connect(self) -> None:
        """Estimate connection."""
        self.conn = self.db.connect()

    def get_tables(self) -> Iterable[str]:
        """Get list of tables."""
        inspector = inspect(self.db)
        print(f"self.conn:{inspector}")
        return [t for t in inspector.get_table_names()]

    def dispose(self) -> None:
        """Dispose opened connections."""
        self.conn.close()
        self.db.dispose()




if __name__=="__main__":
    db_conn = AzureDbConnection(ConnectionSettings)
    sqlcmd = """ select * from information_schema.tables """
    df = pd.read_sql(sqlcmd, db_conn.db)
    print(tabulate(df.head(), headers='keys', tablefmt='psql'))
    #print(tabulate(df, headers='keys', tablefmt='psql'))