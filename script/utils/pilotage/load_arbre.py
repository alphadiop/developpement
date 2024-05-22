# -*- coding: utf-8 -*-
"""
 Load du json d'ordonanacment pour une periodicite
"""

import collections
import os
from collections import OrderedDict
from json import JSONDecoder

#from path import Path
from pathlib import Path

from logger import LOGGER


def load_arbre(periodicite: str, logger: LOGGER = None) -> collections.OrderedDict:
    try:
        path_arbre = os.path.join(Path(os.path.dirname(__file__)).parent.parent.parent,
                                  r'pilotage\arbres\{0}.json'.format(periodicite))
        with open(path_arbre, 'r') as f:
            data = f.read()
        customdecoder = JSONDecoder(object_pairs_hook=OrderedDict)
        return customdecoder.decode(data)
    except Exception as e:
        logger.exception(e)
