#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
a.sort()

min_diff = 2*pow(10,9)+1
i = 0
while i < n-1:
    abs_diff = abs(a[i] - a[i+1])
    if abs_diff < min_diff:
        min_diff = abs_diff
    i += 1
print min_diff
