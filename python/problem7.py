#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def list_prime(x):
    primes = []
    search = list(range(2, x+1))
    top = search.pop(0)
    primes.append(top)
    while top**2 < x:
        search = list(filter(lambda x: x % top != 0, search))
        top = search.pop(0)
        primes.append(top)
    primes.extend(search)
    return primes


print(list_prime(150000)[10001-1])
