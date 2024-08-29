# calculator.py
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

    
def squaresum(n):
    sum_s = 0
    for i in range(1, n+1):
        sum_s = sum_s + (i * i)

    return sum_s


def fact(n):
    if(n==1 or n == 0):
        return 1
    else:
        return n*fact(n-1)

