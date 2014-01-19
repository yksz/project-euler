#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math


def is_square(x2):
    x = int(math.sqrt(x2) + 0.5)
    return x*x == x2


loop = 1000
for a in range(1, loop):
    for b in range(1, loop):
        c2 = a*a + b*b
        if is_square(c2):
            c = int(math.sqrt(c2))
            if a+b+c == 1000:
                print(a, b, c)
                print(a*b*c)
                quit()
