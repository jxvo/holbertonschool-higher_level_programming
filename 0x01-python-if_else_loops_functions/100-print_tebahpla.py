#!/usr/bin/python3
for c in range(-122, -96):
    print("{:c}".format(abs(c) - 32 if abs(c) % 2 != 0 else abs(c)), end="")
