biliothèque python SQLAlchemy
https://www.tutorialsteacher.com/sqlserver/create-database
Il faut enlever le port lorsque le server est local

    def get_connexion_params(self,odbc_driver: str):
        try:
            params = urllib.parse.quote_plus((r'DRIVER={{{odbc_driver}}};' +
                                              'SERVER={server},{port};' +
                                              'DATABASE={database};' +
                                              'UID={username};' +
                                              'PWD={password};'
                                              'MARS_Connection=Yes').format(odbc_driver=odbc_driver,
                                                                            server=self.sql_parameters.get('server'),
                                                                            port=self.sql_parameters.get('port'),
                                                                            database=self.sql_parameters.get('database'),
                                                                            username=self.sql_parameters.get('user'),
                                                                            password=self.sql_parameters.get('password')))
            return params
        except Exception as e:
            self.logger.exception(e)