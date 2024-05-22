
import os
import sys

from path import Path

src_path = os.path.dirname(Path(os.path.abspath(__file__)).parent.parent)
for rep in os.listdir(src_path):
    sys.path.append(os.path.join(src_path, rep))

from indic import Indic
from read_parameters import read_parameters

if __name__ == '__main__':
    try:
        parameters = read_parameters(sys.argv)
        indic = Indic(parameters)
        indic.run_total()
    except Exception as e:
        print(e)
        sys.exit(-1)
