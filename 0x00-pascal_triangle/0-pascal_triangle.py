#!/usr/bin/python3
"""pascal's triangle technical interview"""


def pascal_triangle(n):
    """python technical interview"""
    if n <= 0 or not n:
        return []

    lst_int = []

    for num in range(n):
        var = list(str(11 ** num))
        lst_int += [var]
    return lst_int
