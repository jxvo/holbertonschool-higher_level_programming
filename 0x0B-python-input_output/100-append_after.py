#!/usr/bin/python3
"""Advanced Task 15"""


def append_after(filename="", search_string="", new_string=""):
    """opens a file, and inserts a string where match is found"""
    with open(filename, "r+") as txt_file:
        lines = []
        for line in txt_file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        with open(filename, "w+") as txt_file:
            txt_file.write("".join(lines))
