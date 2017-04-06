#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

while n - 1 > -1:
    print arr[n-1],
    n -= 1
