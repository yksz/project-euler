#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(m, n):  # m >= n
    if n > m:
        return gcd(n, m)
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def lcm(m, n):
    return m * n / gcd(m, n)


x = 1
for i in range(1, 21):
    x = lcm(x, i)
print(x)
