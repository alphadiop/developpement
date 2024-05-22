# -*- coding: utf-8 -*-
import os
from typing import Dict, Union, Tuple

from path import Path

from get_logger import get_logger
from moteurs_stat import get_moteur_source
from statistique import STATISTIQUE
from time_periodes import get_cle_periode
from variable_environnement import get_variable_environnement


class MoteurStatistique(STATISTIQUE):

    def __init__(self, etude_parameters: Dict[str, Union[str, bool]], path_script: str):
        self.etude_parameters = etude_parameters
        self.logger = get_logger(self.etude_parameters,
                                 self.get_path_log_complete(STATISTIQUE.get_path_log(), self.get_sub_paths()),
                                 type_logger=self.etude_parameters.get('TypeLogger', 'stream_file'))

        STATISTIQUE.__init__(self, path_script,self.get_path_json(), logger=self.logger)
        self.path_parameters = self.update_path_parameters(self.path_parameters)

        self.set_parameters_production()

        self.cle_periode = get_cle_periode(self.get_periodicite(), logger=self.logger)
        # self.date_debut, self.date_fin = self.get_range_date()
        self.json_data = self.get_json_data()


    def __str__(self):
        s = "Clas MoteurStatistique"
        s += "  Moteur: " + self.get_moteur(self.etude_parameters)
        s += "  Periodicite: " + self.get_periodicite()
        s += "  Periode: " + self.get_periode()
        s += "  Path du script de lancement: " + self.path_script
        return s


    def get_periodicite(self) -> str:
        return self.etude_parameters['Periodicite']

    def get_periode(self) -> str:
        return self.etude_parameters['Periode']

    def get_sub_paths(self) -> str:
        periodes = self.get_path_save_levels()
        return os.path.join(self.get_moteur(self.etude_parameters), self.get_periodicite(), periodes[0], periodes[1])

    def get_path_save_levels(self) -> Tuple[str, str]:
        return self.get_periode()[:4], self.get_periode()[-2:]

    def set_parameters_production(self):
        keys = ['IsProduction', 'IsReprise', 'IsRelance']
        for key in keys:
            if key not in self.etude_parameters.keys():
                self.etude_parameters[key] = False


    def update_path_parameters(self, path_parameters: Dict[str, Union[str, Dict[str, str]]]):
        path_parameters['calls'] = get_variable_environnement(self.variable_environnement, variable='calls', logger=self.logger)
        path_parameters['save'] = self.get_path_save()
        path_parameters['data_figees'] = get_variable_environnement(self.variable_environnement, variable='data_figees',logger=self.logger)
        return path_parameters

    def get_path_save(self):
        periode = self.get_path_save_levels()
        return os.path.join(Path(self.path_script).parent.parent,
                            get_variable_environnement(self.variable_environnement, variable='data'),
                            self.get_moteur(self.etude_parameters), self.get_periodicite(), periode[0], periode[1])


    def get_path_json(self) -> str:
        try:
            return os.path.join('sql_queries',
                                get_moteur_source(self.moteurs_stat, self.get_moteur(self.etude_parameters),
                                                  self.get_periodicite()) + '.json')
        except Exception as e:
            self.logger.exception(e)