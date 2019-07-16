#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = []
    for idx in my_list:
        new_list.append(idx % 2 == 0)
    return new_list
