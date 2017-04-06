#!/bin/python

from collections import defaultdict

n = int(raw_input().strip())
d = defaultdict(int)

for i in xrange(n):
    d[raw_input().strip()] += 1

q = int(raw_input().strip())

for j in xrange(q):
    print d[raw_input().strip()]