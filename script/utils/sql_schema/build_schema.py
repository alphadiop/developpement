# -*- coding: utf-8 -*-
"""
 Fonctions de construction d'un schema à partir de la définition json
"""

from typing import List, Tuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logger import LOGGER


def build_schema(json_schema: dict, format: dict = None, logger: 'LOGGER' = None) -> List[Tuple[str, str, str]]:
    """Construction d'un schema sql sous la forme d'une list de tuple

    :param json_schema: schema sous forme d'un dictionnaire python
    :param format: list de format (facultative)
    :param logger: gestionnaire de logs (facultative)
    :return: schema
    """
    try:
        if format is None:
            format = dict()
        return [(column.format(**format), info['sql_type'], info['nullable']) for column, info in json_schema.items()]
    except Exception as e:
        logger.exception(e)
