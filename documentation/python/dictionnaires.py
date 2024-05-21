import time
moteur = "dico"
import logging

import sys
import logging
import colorlog

log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
logging.basicConfig(filename="log.log",format=log_format,filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)
##logger.addHandler(logging.FileHandler('log.log'))


dico = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])


def my_timer(original_function):
    def _timer(*args, **kwargs):
        logger.info("{0} : {1} - START".format(moteur, original_function.__name__).upper())
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time()
        logger.info("{0} : {1} - END - Elapsed Time = {2}".format(moteur, original_function.__name__, end - start).upper())
        return result
    return _timer
@my_timer
def afficher_dico(d):
    liste_keys = [key for key in d.keys()]
    liste_values = [key for key in d.values()]
    return liste_values


if __name__ == "__main__":
    logger = logging.getLogger('simpleExample')
    logger.info('info message')
    #logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    afficher_dico(dico)


