#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, "r") as txt:
        count = 0
        for line in txt:
            if nb_lines <= 0 or count < nb_lines:
                print(line, end="")
                count += 1
