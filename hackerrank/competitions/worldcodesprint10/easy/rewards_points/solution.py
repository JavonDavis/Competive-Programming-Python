#!/bin/python

import sys

def getPoints(month1, month2, month3):
    month1 = min(month1, 10)
    month2 = min(month2, 10)
    month3 = min(month3, 10)
    return month1*10 + month2*10 + month3*10

month1,month2,month3 = raw_input().strip().split(' ')
month1,month2,month3 = [int(month1),int(month2),int(month3)]
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)
