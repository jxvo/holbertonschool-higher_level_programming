#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rvsd = my_list[::-1]
    for i in rvsd:
        print("{:d}".format(i))
