# -*- coding: utf-8 -*-
"""
 Class LOGGER
"""

import logging
import os
import sys
from typing import Dict

import sqlparse

from random_string import random_string
from tabulate_dataframe import tabulate_dataframe


class LOGGER:

    def __init__(self, etude_parameters: Dict[str, str], path_log: str, level: str = 'INFO',
                 type_logger: str = "stream", format: str = None):
        self.etude_parameters = etude_parameters
        self.level = self.get_level(level)
        self.format = self.get_format(format)

        self.path_log, self.path_sql = self.get_path_logs(path_log)
        self.logger = self.create_logger()
        self.handlers = self.create_handlers(type_logger)
        self.set_formatter_to_handler()
        self.add_handler_to_logger()

        self.sql_logger = self.get_file_handler()

    def __str__(self):
        s = "class LOGGER \n"
        s += "  Level: {0}\n".format(self.level)
        s += "  Logger: {0}\n".format(self.logger)
        s += "  Handlers: {0}\n".format(self.handlers)
        return s

    @staticmethod
    def get_format(format: str):
        return '\n %(asctime)s - %(levelname)s - %(message)s' if format is None else format

    @staticmethod
    def get_level(level):
        if level == "INFO":
            return logging.INFO
        elif level == "WARNING":
            return logging.WARNING
        elif level == "DEBUG":
            return logging.DEBUG

    def create_logger(self):
        logging.basicConfig(level=self.level)
        return logging.getLogger(random_string())

    def create_handlers(self, type_logger: str):
        handlers = list()
        if 'stream' in type_logger:
            handlers.append(logging.StreamHandler())
        if "file" in type_logger:
            handlers.append(logging.FileHandler(self.path_log, mode='a', encoding="utf-8"))
        for handler in handlers:
            handler.setLevel(self.level)
        return handlers

    def add_handler_to_logger(self):
        self.logger.propagate = False
        for handler in self.handlers:
            self.logger.addHandler(handler)

    def set_formatter_to_handler(self):
        formatter = logging.Formatter(self.format)
        for handler in self.handlers:
            handler.setFormatter(formatter)

    def get_path_logs(self, path_logs: str):
        if not os.path.exists(path_logs):
            os.makedirs(path_logs)
        else:
            for content in os.listdir(path_logs):
                path = os.path.join(path_logs, content)
                extensions = ['OK', 'NOOK', 'sql']
                file_exists = ['.'.join([self.etude_parameters['Moteur'], extension]) for extension in extensions]
                if os.path.isfile(path) and content in file_exists:
                    os.remove(path)
                # else:
                #     shutil.rmtree(path)

        path_log = os.path.join(path_logs, "{0}.NOOK".format(self.etude_parameters['Moteur']))
        path_sql = os.path.join(path_logs, "{0}.sql".format(self.etude_parameters['Moteur']))
        return path_log, path_sql

    def shutdown(self):
        self.remove_handlers()
        logging.shutdown()

    def remove_handlers(self):
        for handler in self.handlers:
            handler.close()
            self.logger.removeHandler(handler)

    def info(self, msg: str):
        self.logger.info(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)

    def error(self, msg: str, exc_info: bool = False):
        self.logger.error(msg, exc_info=exc_info)

    def exception(self, e: Exception = None):
        if e is not None:
            self.logger.error(e, exc_info=True)
        self.logger.error("!!! Le programme s'est arrêté sur une erreur !!!")
        self.remove_handlers()
        sys.exit(-1)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def rename_path_log(self, suffix: str) -> None:
        src_path_log = self.path_log
        dst_path_log = self.path_log.replace('NOOK', suffix)
        os.rename(src_path_log, dst_path_log)

        self.path_log = dst_path_log

    def get_file_handler(self):
        return open(self.path_sql, "w")

    def close(self):
        self.shutdown()
        self.sql_logger.close()

    def write_moteur_properties(self, path_save: str) -> None:
        self.logger.info("="*120 + '\n')
        self.logger.info(" Propriétés du moteur:")
        for key, value in self.etude_parameters.items():
            if key != 'Panier':
                self.logger.info(" "*3 + "{0}: {1}".format(key, value))
        if 'Panier' in self.etude_parameters.keys():
            self.logger.info('Panier: \n' + tabulate_dataframe(self.etude_parameters['Panier']))
        self.logger.info(" "*3 + "Dir save: {0}".format(path_save))
        self.logger.info(" "*3 + "Path log: {0}".format(self.path_log.replace('INPROGRESS', 'OK/NOOK')))
        self.logger.info(" "*3 + "Path sql: {0}".format(self.path_sql))
        self.logger.info("="*120 + '\n')

    def write_sql_properties(self, sql_parameters) -> None:
        self.sql_logger.write('\n' + "-- " + "="*120 + '\n')
        self.sql_logger.write("-- Propriétés de la connexion SQL:\n")
        self.sql_logger.write("--" + " "*3 + "Server: {0}\n".format(sql_parameters["server"]))
        self.sql_logger.write("--" + " "*3 + "Database: {0}\n".format(sql_parameters["database"]))
        self.sql_logger.write("--" + " "*3 + "Port: {0}\n".format(sql_parameters["port"]))
        self.sql_logger.write("-- " + "="*120 + '\n')

    def write_sql_query(self, query: str, reindent=True):
        if self.sql_logger is not None:
            self.sql_logger.write("\n\n{0}".format(sqlparse.format(query, reindent=reindent, keyword_case='upper',
                                                                   strip_comments=True)))
