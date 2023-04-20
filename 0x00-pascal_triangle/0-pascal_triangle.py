#!/usr/bin/python3
"""pascal's triangle technical interview"""
from math import factorial


def pascal_triangle(n):
    # """python technical interview"""
    if n <= 0 or not n:
        return []

    lst_int = []
    for num in range(n):
      var = [int(x) for x in list(str(11 ** num))]
      lst_int += [var]
    return lst_int

    # lst_int = []

    # for i in range(n):

    #     row = []
    #     for j in range(i+1):

    #         # nCr = n!/((n-r)!*r!)
    #         row += [factorial(i)//(factorial(j)*factorial(i-j))]
    #     lst_int += [row]
    # return lst_int
