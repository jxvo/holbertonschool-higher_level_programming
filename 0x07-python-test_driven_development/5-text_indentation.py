#!/usr/bin/python3
def text_indentation(text):
    """parse string and add two newlines after '.' '?' and ':' chars"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    indent_chars = ('.', '?', ':')
    start_idx = 0

    for idx, current_char in enumerate(text):
        if current_char in indent_chars:
            print(text[start_idx:idx + 1].strip() + '\n')
            start_idx = idx + 1
    print(text[start_idx:].strip(), end="")
