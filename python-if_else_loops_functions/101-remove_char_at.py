#!/usr/bin/env python3
def remove_char_at(str, n):
    """Function that removes a character at a specific index in a string.

    Args:
        str (str): The string to remove the character from.
        n (int): The index of the character to remove.

    Returns:
        str: The string with the character at index n removed.
    """
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
