#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    pascal = [1]
    for row in range(n):
        triangle.append(pascal)
        temp_list = []
        temp_list.append(pascal[0])
        for idx in range(len(pascal) - 1):
            temp_list.append(pascal[idx] + pascal[idx + 1])
        temp_list.append(pascal[-1])
        pascal = temp_list
    return triangle
