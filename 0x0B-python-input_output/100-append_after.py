#!/usr/bin/python3
"""Advanced Task 15"""


def append_after(filename="", search_string="", new_string=""):
    """opens a file, parses each line to match string, and inserts new string"""
    with open(filename, "r+") as txt_file:
        lines = txt_file.readlines()
        for idx in range(len(lines)):
            if search_string in lines[idx]:
                lines.insert(idx + 1, new_string)
        with open(filename, "w+") as txt_file:
            txt_file.write("".join(lines))
