# -*- coding: utf-8 -*-
"""
 Test Class SqlManagement:
"""

import sys

import pyodbc
import pytest

for path in sys.path:
    print(path)


from sql_manager import SQLManager


@pytest.fixture
def sql_operations():
    return SQLManager(server_name='dw_gersit', odbc_driver='ODBC Driver 17 for SQL Server')


class TestSQLManager:

    def test_sql_manager(self, sql_operations):
        assert isinstance(sql_operations.connexion, pyodbc.Connection)
