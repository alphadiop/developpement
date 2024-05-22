
from typing import List, Tuple

from logger import LOGGER


def print_logger(language: str, type: str, checks: List[Tuple[str, str, str, str]], logger: LOGGER) -> None:
    logger.info('\n\n{0} {1}:'.format(language, type.lower()))

    headers = (' {0} '.format(type), ' Requis ', ' Actuel ', ' ')

    format = {head: max([len(head)] + [len(check[ind]) for check in checks]) for ind, head in enumerate(headers)}

    logger.info('\n')
    logger.info('  |' + '|'.join([head.center(format[head], ' ') for head in format.keys()]) + '|')
    logger.info('  |' + '|'.join(['-'*format[head] for head in format.keys()]) + '|')

    for check in checks:
        logger.info('  |' + '|'.join([check[ind].center(format[head]) for ind, head in enumerate(headers)]) + '|')