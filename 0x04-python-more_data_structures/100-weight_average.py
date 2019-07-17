#!/usr/bin/python3
def weight_average(my_list=[]):
    score, weight  = 0, 0

    if not my_list:
        return 0
    for w_s in my_list:
        score += w_s[0] * w_s[1]
        weight += w_s[1]
    return number / count
