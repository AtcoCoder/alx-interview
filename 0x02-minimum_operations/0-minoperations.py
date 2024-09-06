#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file
    """
    if n <= 1:
        return 0
    primes = [2, 3, 5, 7, 11, 13]
    if n in primes:
        return n
    
    for prime in primes:
        if n % prime == 0:
            return int(prime + minOperations(n / prime))
        return n
