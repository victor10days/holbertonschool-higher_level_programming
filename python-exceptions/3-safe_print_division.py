#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.
    Returns:
        float: The result of the division. If division by zero occurs, returns None.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
