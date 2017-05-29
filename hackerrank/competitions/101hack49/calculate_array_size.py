#!/bin/python

import sys

def getArrayKb(n, d):
    return reduce(lambda x, y: x*y, d)*4/1024

#  Return the size of the multidimensional array in kilobytes. Return only the integer part.
n = int(raw_input().strip())
d = map(int, raw_input().strip().split(' '))
result = getArrayKb(n, d)
print(result)
