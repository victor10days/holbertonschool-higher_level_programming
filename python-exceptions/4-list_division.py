#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list of numbers.
        my_list_2 (list): The second list of numbers.
        list_length (int): The number of elements to consider from both lists.

    Returns:
        list: A new list containing the results of the division. If division
        cannot be performed for an element, the result is None for that element.
    """
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            division = 0
            print("wrong type")
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            result.append(division)
    return result
