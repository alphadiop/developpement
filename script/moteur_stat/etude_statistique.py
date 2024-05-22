import os

from get_logger import get_logger
from statistique import STATISTIQUE
from typing import Dict, Union

class EtudeStatistique(STATISTIQUE):

    def __init__(self, etude_parameters: Dict[str, str], path_script):
        self.etude_parameters = etude_parameters
        self.composition_data = self.load_composition_data()
        #self.logger = get_logger(parameters={'Moteur': etude_parameters['Etude']},self.get_path_log_complete(STATISTIQUE.get_path_log(), self.get_sub_paths()))

        STATISTIQUE.__init__(self, path_script, self.get_path_json(), self.logger)
        self.json_data = self.get_json_data()


    def load_composition_data(self):
        pass

    def get_path_json(self) -> str:
        try:
            return os.path.join('sql_queries', self.get_moteur(self.etude_parameters) + '.json')
        except Exception as e:
            self.logger.exception(e)