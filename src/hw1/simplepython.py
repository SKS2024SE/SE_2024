# calculator.py
"""Module is used to calculate few math functions."""

from math import sqrt

def is_prime(n):
    """Module is used to calculate few math functions."""

    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def squaresum(n):
    """Module is used to calculate few math functions."""

    sum_s = 0
    for i in range(1, n+1):
        sum_s = sum_s + (i * i)

    return sum_s

def fact(n):
    """Module is used to calculate few math functions."""
    if n in(1,0):

        return 1
    return n*fact(n-1)
