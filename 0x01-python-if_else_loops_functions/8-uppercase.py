#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        print("{:c}".format(i - 32 if i >= 96 and i <= 122 else i), end="")
    print()
