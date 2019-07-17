#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception("Too far")
            else:
                ans += a ** b / n
        except:
            return a + b
    return ans
