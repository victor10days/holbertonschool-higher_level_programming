#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    max_int = my_list[0]
    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int
