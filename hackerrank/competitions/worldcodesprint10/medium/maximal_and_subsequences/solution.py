#!/bin/python

import sys
from math import factorial

import operator as op

def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

# def nCr(n,r):
#     f = factorial
#     return f(n) / f(r) / f(n-r)

def solve(n, k, a):
    # a = ["{:060b}".format(x) for x in a]
    limit = 61 # chosen based on 10^18 constraint on ai in prob statement
    one_count = [ set() for _ in xrange(limit)]
    result = set()
    for i in xrange(n):
        a_i = "{:061b}".format(a[i])
        for j in xrange(limit):
            if a_i[j] == "1":
                one_count[j].add((a_i, i))
        result.add((a_i, i))
    # print one_count
    for one_set in one_count:
        if len(result&one_set) >= k:
            result &= one_set
    # print result
    if len(result) == 0:
        num_results = nCr(n, k)
        return 0, num_results % (pow(10, 9) + 7)
    result = [long(x[0], 2) for x in result]
    result_value = reduce(lambda x,y: x& y, result)
    num_results = nCr(len(result), k)
    return result_value, num_results % (pow(10, 9) + 7)



n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = []
a_i = 0
for a_i in xrange(n):
    a_t = long(raw_input().strip())
    a.append(a_t)
result = solve(n, k, a)
print "\n".join(map(str, result))
#
# p = pow(10, 5)
# sample = range(p)
# print solve(p,3, sample)
# print solve(3, 2, [21, 2, 2])
