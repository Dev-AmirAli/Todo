
"""Config Database"""

MSSQL = {'host': 'localhost',
         'user': 'root',
         'passwd': 'root',
         'port': '3306',
         'db': 'mydb'}

POSTGRES = {'host': 'localhost',
            'user': 'postgres',
            'passwd': 'postgres',
            'db': 'mydb'}

MSQL_CONFIG = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(MSSQL['user'], MSSQL['passwd'], MSSQL['host'],
                                                             MSSQL['port'], MSSQL['db'])

POSTGRES_CONFIG = "postgresql+psycopg2://{}:{}@{}/{}".format(POSTGRES['user'], POSTGRES['passwd'], POSTGRES['host'],
                                                             POSTGRES['db'])


