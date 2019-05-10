#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    maxx = my_list[0]
    for num in my_list:
        if num > maxx:
            maxx = num
    return maxx
