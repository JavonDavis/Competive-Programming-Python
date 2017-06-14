#!/bin/python

import sys


def twinArrays(arr1, arr2):
    arr1 = [(arr1[index], index) for index in xrange(len(arr1))]
    arr2 = [(arr2[index], index) for index in xrange(len(arr2))]
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    pair = arr1[0], arr2[0]
    if pair[0][1] == pair[1][1]:
        return min(pair[0][0] + arr2[1][0], pair[1][0] + arr1[1][0])
    return pair[0][0] + pair[1][0]


n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)
