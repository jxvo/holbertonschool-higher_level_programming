#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = []

    for row in range(1, n + 1):
        pascal.append(1)
        for idx in range(row - 2, 0, -1):
            pascal[idx] += pascal[idx -1]
    return pascal
