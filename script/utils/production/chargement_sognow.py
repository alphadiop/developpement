# -*- coding: utf-8 -*-
"""
 Script de dépôt sur S3 des données SOGNOW
"""

import os
import sys

from path import Path

src_path = os.path.dirname(Path(os.path.abspath(__file__)).parent.parent)
for rep in os.listdir(src_path):
    sys.path.append(os.path.join(src_path, rep))

from chargement_s3_sognow import ChargementS3Sognow
from read_parameters import read_parameters

if __name__ == '__main__':
    try:
        parameters = read_parameters(sys.argv)
        chargement = ChargementS3Sognow(parameters)
        chargement.run()
        print(chargement.get_bucket_key())
    except Exception as e:
        print(e)
        sys.exit(-1)
