import os
from typing import List, Tuple

from load_json import load_json
from sql_schema import get_list_data_figees
from sql_schema import build_schema
from time_periodes import get_cle_periode


def adiop_get_schema_from_json(path_schema: str, table: str, periodicite: str = None, columns: List[str] = None,
                         format: dict = None, logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:

    json_schema = dict()
    tables_figees = get_list_data_figees('data_figees')
    if table in tables_figees:
        json_schema.update(load_json(os.path.join(path_schema, 'data_figees', f'{table}.json'), logger=logger))

    cle_periode = get_cle_periode(periodicite, logger=logger)

    format = {'ClePeriode': cle_periode} if format is None else {**{'ClePeriode': cle_periode}, **format}

    schema = build_schema(json_schema, format=format, logger=logger)

    if columns is not None:
        schema = list(filter(lambda tp: tp[0] in columns, schema))

    return schema