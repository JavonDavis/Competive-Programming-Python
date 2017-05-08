#!/bin/python

import sys

def best_choice(arr):
    n = len(arr)
    a_sum = sum(arr)
    best_i = 0
    best_r = 0
    for i in xrange(n):
        el = arr[i]
        if a_sum % el > best_r:
            best_i = i
            best_r = (a_sum - el) % el
    return best_r, best_i

def getMaxScore(a):
    total_sum = 0
    while a:
        r, i = best_choice(a)
        a.pop(i)
        print r
        total_sum += r
    return total_sum


def test(arr):
    s = 0
    n = len(arr)
    chosen = [0]*n
    for k in xrange(n):
        inner = 0
        for i in xrange(k-1):
            inner += arr[i]
        max_inner = 0
        c = None
        for j in xrange(k-1, n):
            if inner % arr[k] >= max_inner and chosen[k] != 1:
                max_inner = inner % arr[k]
                c = k
        chosen[c] = 1
        s += max_inner
    return s



n = int(raw_input().strip())
a = map(long, raw_input().strip().split(' '))
# maxScore = getMaxScore(a)
# print(maxScore)
print test(a)
