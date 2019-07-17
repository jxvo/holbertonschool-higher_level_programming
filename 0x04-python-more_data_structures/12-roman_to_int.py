#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    num = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for idx in range(len(roman_string)):
        if idx > 0 and roman[roman_string[idx]] > roman[roman_string[idx - 1]]:
            num += roman[roman_string[idx]] - 2 * roman[roman_string[idx - 1]]
        else:
            num += roman[roman_string[idx]]
    return num
