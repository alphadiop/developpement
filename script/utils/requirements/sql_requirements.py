# -*- coding: utf-8 -*-
"""
 Verification de la presence du drive odbc attendu
"""

from typing import TYPE_CHECKING
from typing import Tuple, List

import pandas as pd
import pyodbc

from variable_environnement import get_variable_environnement

if TYPE_CHECKING:
    from logger import LOGGER


def sql_requirements(variable_environnement: pd.DataFrame, logger: 'LOGGER') -> str:
    driver = get_variable_environnement(variable_environnement, 'odbc_driver', logger)
    check_sql = (driver, 'OK' if driver in available_odbc_drivers() else 'NOOK')
    sql_print(check_sql, logger)

    if check_sql[1] == 'OK':
        return ''
    else:
        return 'ODBC Driver disponible(s): {0}'.format(str(available_odbc_drivers()))


def sql_print(check_sql: Tuple[str, str], logger: 'LOGGER') -> None:
    logger.info('\n\nODBC Driver:')

    headers = (' Driver ', ' ')

    format = {head: max([len(head)] + [len(check_sql[ind])]) for ind, head in enumerate(headers)}

    logger.info('\n')
    logger.info('  |' + '|'.join([head.center(format[head], ' ') for head in format.keys()]) + '|')
    logger.info('  |' + '|'.join(['-'*format[head] for head in format.keys()]) + '|')
    logger.info('  |' + '|'.join([check_sql[ind].center(format[head]) for ind, head in enumerate(headers)]) + '|')


def available_odbc_drivers() -> List[str]:
    return list(filter(lambda driver: 'ODBC' in driver, pyodbc.drivers()))
