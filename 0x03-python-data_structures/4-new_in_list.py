#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return my_list
    newby = my_list.copy()
    newby[idx] = element
    return newby
