#!/usr/bin/python3
"""
pascal_triangle
"""

def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n:
    """
    list_of_rows = []
    if n <= 0:
        return list_of_rows
    
    list_of_rows.append([1])
    row_number = 1
    if n > 1:
        current_row = [1, 1]
        list_of_rows.append(current_row)
        row_number += 1
    
    while (row_number < n):
        new_row = [1]
        for i in range(len(current_row)):
            if (i + 1) < len(current_row):
                current_num = current_row[i]
                next_num = current_row[i + 1]
                new_row.append(current_num + next_num)
        new_row.append(1)
        list_of_rows.append(new_row)
        current_row = new_row
        row_number += 1
    
    return list_of_rows