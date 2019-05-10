#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for name, value in sorted(a_dictionary.items(), key=lambda p: p[0]):
        print("{:s}: {}".format(name, value))
