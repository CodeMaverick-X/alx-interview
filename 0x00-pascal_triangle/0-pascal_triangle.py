#!/usr/bin/python3
"""
Pascal's Triangle modile water
they have greater school we dont
"""


def pascal_triangle(n):
    """computes, try dilivtor
    """
    if n <= 0:
        return []
    triangle = [[1]]
    idx = 0

    for i in range(1, n):
        prevs = triangle[idx]
        row = [1]
        for j in range(1, len(prevs)):
            row.append(prevs[j-1] + prevs[j])
        row.append(1)
        idx += 1
        triangle.append(row)
    return triangle
