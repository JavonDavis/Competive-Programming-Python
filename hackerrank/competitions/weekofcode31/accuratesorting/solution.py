#!/bin/python

import sys


def sort(arr):
    if len(arr) == 1:
        return True

    for i in xrange(len(arr) - 1):
        if arr[i] - arr[i + 1] == 1:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    can_be_sorted = sort(a)
    if can_be_sorted:
        print "Yes"
    else:
        print "No"

