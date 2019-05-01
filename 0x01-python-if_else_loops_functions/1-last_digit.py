#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
d = number % 10
if number < 0:
    d = (abs(number) % 10) * -1
if d > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, d))
elif d == 0:
    print("Last digit of {} is {} and is 0".format(n, d))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, d))
