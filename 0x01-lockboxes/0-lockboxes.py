#!/usr/bin/python3
"""
n number of locked boxes, numberred sequnetially form 0 to n-1
and may contain keys to other boxes. Method to determine if all boxes can open
"""


def canUnlockAll(boxes):
    """method to determine if all boxes can open"""
    count = 0
    n = len(boxes)
    
    for idx in range(1, n):
        for num, box in enumerate(boxes):
            if idx in box and idx != num:
                count += 1
                break
    if count >= n - 1:
        return True
    return False
