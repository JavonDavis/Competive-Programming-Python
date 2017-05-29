#!/bin/python

import sys


def getMaxBridges(x1, y1, x2, y2, xC, yC):

    left_right = min(xC - x1, x2 - xC)
    up_down = min(yC - y1, y2 - yC)
    diagonals = left_right* up_down * 2
    return left_right + up_down + diagonals

#  Return the maximum number of bridges the Rulers will commission.
x1, y1 = raw_input().strip().split(' ')
x1, y1 = [long(x1), long(y1)]
x2, y2 = raw_input().strip().split(' ')
x2, y2 = [long(x2), long(y2)]
xC, yC = raw_input().strip().split(' ')
xC, yC = [long(xC), long(yC)]
result = getMaxBridges(x1, y1, x2, y2, xC, yC)
print(result)
