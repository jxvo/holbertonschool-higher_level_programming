#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, NameError, TypeError):
            continue
        else:
            num += 1
    print()
    return num
