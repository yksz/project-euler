#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def is_square(x2):
    x = int(math.sqrt(x2) + 0.5)
    return x*x == x2


def fermat_factor(n):  # n should be odd
    a = math.ceil(math.sqrt(n))
    b2 = a*a - n
    while not is_square(b2):
        a += 1
        b2 = a*a - n
    b = math.sqrt(b2)
    x = int(a - b)
    y = int(a + b)
    return x, y


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def fermat_factors(n, lst):
    x, y = fermat_factor(n)
    if is_prime(x):
        lst.append(x)
    else:
        fermat_factors(x, lst)
    if is_prime(y):
        lst.append(y)
    else:
        fermat_factors(y, lst)


def prime_factors(n):
    lst = []
    fermat_factors(n, lst)
    return lst


lst = prime_factors(600851475143)
print(lst)
print("max:", max(lst))
