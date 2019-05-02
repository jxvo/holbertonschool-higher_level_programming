#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        print("{:d}{:d}".format(a, b), end="\n" if a == 8 and b == 9 else ", ")
