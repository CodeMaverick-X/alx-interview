#!/usr/bin/python3
"""lock boxes interview task
"""


def canUnlockAll(boxes):
    lenght = len(boxes)
    opn_box = set()
    opn_box.add(0)

    for x in range(lenght):
        init_len = len(opn_box)
        for index, box in enumerate(boxes):
            if index not in opn_box:
                continue
            for item in box:
                if item < lenght and item >= 0:
                    opn_box.add(item)
        new_len = len(opn_box)
        if new_len == init_len:
            break

    len_set = len(opn_box)
    if len_set == lenght:
        return True
    else:
        return False
