#!/bin/python

import sys


def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def getMagicNumber(s, k, b, m):

    loop_invariant = 0
    exp = k -1
    # precompute invariant
    for i in xrange(k):
        loop_invariant += (pow_mod(b, exp, m) * int(s[i]))
        exp -= 1

    total = loop_invariant % m
    start = 0
    end = k

    while end < len(s):
        highest_bit = (pow_mod(b, k-1, m) * int(s[start])) %m
        new_bit = int(s[end]) % m


        loop_invariant -= highest_bit
        loop_invariant *= (b%m)
        loop_invariant += new_bit
        loop_invariant %= m
        total += loop_invariant
        start += 1
        end += 1
    return total


s = raw_input().strip()
k, b, m = raw_input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
