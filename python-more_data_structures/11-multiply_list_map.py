#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all elements multiplied by a given number."""
    return list(map(lambda x: x * number, my_list))
