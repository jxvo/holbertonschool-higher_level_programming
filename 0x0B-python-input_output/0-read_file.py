#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r") as txt:
        print(txt.read())
    txt.closed
