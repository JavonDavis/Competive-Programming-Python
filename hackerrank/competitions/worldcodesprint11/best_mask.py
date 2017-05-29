#!/bin/python

import sys


def getMagicNumber(s, k, b, m):

    loop_invariant = 0
    exp = k -1
    # precompute invariant
    for i in xrange(k):
        loop_invariant += (b**exp * int(s[i]))
        exp -= 1

    total = loop_invariant % m
    start = 0
    end = k

    while end < len(s):
        highest_bit = (b**(k-1) * int(s[start]))
        new_bit = int(s[k])

        loop_invariant -= highest_bit
        loop_invariant *= b
        loop_invariant += new_bit
        total += loop_invariant % m
        end += 1
    return total


s = raw_input().strip()
k, b, m = raw_input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
