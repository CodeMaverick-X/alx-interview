#!/usr/bin/python3
"""
Module that gets the Minimum Operations
"""


def minOperations(n):
    """calculate sthe fewest number of operations needed
     to result in exactly n H CHAR IN THe file"""

    ops_d = {'copyAll': 0, 'paste': 0}
    file_len = 1

    while file_len < n:
        if n % file_len == 0:
            ops_d['copyAll'] += 1
            clipboard = file_len
        ops_d['paste'] += 1
        file_len += clipboard
    return sum(ops_d.values())
