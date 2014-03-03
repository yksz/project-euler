#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[-1]
    else:
        if s[0] == s[-1]:
            return is_palindromic(s[1:-1])
        else:
            return False

lst = []
for x in range(100, 1000):
    for y in range(100, 1000):
        n = x * y
        if is_palindromic(str(n)):
            lst.append(n)
print(max(lst))
