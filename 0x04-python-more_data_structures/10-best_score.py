#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        return max(a_dictionary.items(), key=lambda i: i[1])[0]
