# -*- coding: utf-8 -*-
"""
 get de la class SQL_Alchemy
"""

from typing import TYPE_CHECKING

from sql_operations import SQLOperations
from variable_environnement import get_variable_environnement
from variable_environnement import load_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def get_sql_operations(server_name: str = None, odbc_driver: str = None, connect_args: dict = None,
                       options: dict = None, logger: 'LOGGER' = None) -> 'SQLOperations':
    if server_name is None:
        server_name = 'dw_gersit'

    if odbc_driver is None:
        variable_environnement = load_variable_environnement(logger=logger)
        odbc_driver = get_variable_environnement(variable_environnement, variable='odbc_driver', logger=logger)

    if connect_args is None:
        connect_args = {'autocommit': True}

    return SQLOperations(server_name, odbc_driver, connect_args=connect_args, options=options, logger=logger)
