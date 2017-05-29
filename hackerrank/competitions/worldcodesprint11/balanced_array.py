#!/bin/python

import sys


def solve(a):
    # type: (int) -> int
    left_sum, right_sum = sum(a[:n/2]), sum(a[n/2:])
    return max(right_sum, left_sum) - min(right_sum, left_sum)


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = solve(a)
print(result)
