#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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

primes = list_prime(2000000)
print(sum(primes))
