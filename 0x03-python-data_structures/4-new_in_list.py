#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx >= 0 or len(my_list) >= idx:
        new_list[idx] = element
    return new_list
