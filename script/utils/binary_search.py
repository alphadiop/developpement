# -*- coding: utf-8 -*-
"""
 Binary search of a number within a list in Python
"""


def binary_search(a_list, item) -> bool:
    """Recherche binaire d'un element "itemé dans une liste 'a_list'

    :param a_list: liste d'items
    :param item: items dont on souhaite cherché l'occurence dans une liste
    :return: True si l'item est présent sinon False
    """
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
