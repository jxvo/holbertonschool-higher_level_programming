#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r") as txt:
        for line in txt:
            print(line, end="")
    txt.closed
