#!/usr/bin/python3
"""contains func that makes change"""


def makeChange(coins, total):
    """makes cahnge with the fewest coin to make
    up total"""
    if total <= 0:
        return 0
    sort_coin = sorted(coins, reverse=True)
    len_c = len(coins)
    count = 1
    val = log = new_val = 0
    while val < len_c:
        if (count * sort_coin[val] + new_val) > total:
            log += count - 1
            new_val += sort_coin[val] * (count - 1)
            val += 1
            count = 1
        else:
            count += 1
        if new_val == total:
            return log
    return -1
