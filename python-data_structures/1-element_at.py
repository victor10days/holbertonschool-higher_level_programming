#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list like in C.

    Args:
        my_list (list): List of elements.
        idx (int): Index of the element to retrieve.

    Returns:
        The element at the specified index or None if index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
