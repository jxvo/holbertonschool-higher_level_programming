#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = (abs(number) % 10) * -1
print("Last digit of {:d} is {:d}".format(number, last), end = " ")
if last > 5:
    print("and is greater than 5")
elif last < 6 and last != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
