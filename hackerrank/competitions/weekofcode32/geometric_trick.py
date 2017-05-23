#!/bin/python

import sys


def findGeometricTriplets(arr):
    for j in xrange(1, n):
        i = j - 1
        k = j + 1
        while i >= 0 and k <= n - 1:
            while (arr[j] % arr[i] == 0 and
                               arr[k] % arr[j] == 0 and
                               arr[j] / arr[i] == arr[k] / arr[j]):
                print "{} {} {}".format(arr[i], arr[j], arr[k])

                k += 1
                i -= 1

            if arr[j] % arr[i] == 0 and arr[k] % arr[j] == 0:
                if arr[j] / arr[i] < arr[k] / arr[j]:
                    i -= 1
                else:
                    k += 1
            elif arr[j] % arr[i] == 0:
                k += 1
            else:
                i -= 1


def geometricTrick(s):
    indices = range(1, len(s) + 1)
    findGeometricTriplets(indices)


n = int(raw_input().strip())
s = raw_input().strip()
result = geometricTrick(s)
print(result)
