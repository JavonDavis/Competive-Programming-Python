#!/bin/python

n, d = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

d = d % n

for i in xrange(n):
    print arr[(d + i) % n],
