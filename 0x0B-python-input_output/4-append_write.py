#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a") as txt:
        return txt.write(text)
