#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    with open(filename, "r") as txt:
        for line in txt:
          count += 1
    return count
