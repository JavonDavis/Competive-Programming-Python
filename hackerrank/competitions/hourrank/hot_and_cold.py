#!/bin/python

import sys

def isSatisfiable(c1, c2, h1, h2):
    if range(max(c1, c2), min(h1,h2)+1) != []:
        return "YES"
    else:
        return "NO"

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = raw_input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)
