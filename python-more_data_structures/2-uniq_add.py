#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    unique_elements = set(my_list)
    for num in unique_elements:
        unique_sum += num
    return unique_sum
