#!/bin/python

import sys

# Nice algo to loop subsets
def solve(n, a):
    bit_array = [0 for _ in xrange(n)]
    bit_array[n-1], bit_array[n-2], bit_array[n-3] = 1, 1, 1
    subset_rep = snoob(7) # Decides length of subset
    while len(subset_rep) <= n:
        subset_rep = snoob(int(subset_rep, 2))
    print "done"


def snoob(x):
    smallest = x & -x
    ripple = x + smallest
    ones = x ^ ripple
    ones = (ones >> 2)/smallest
    return "{0:b}".format(ripple | ones)

def nexthi_same_count_ones(a):
  c = (a & -a);
  r = a+c;
  return ((((r ^ a) >> 2) / c) | r)


solve(pow(10, 5)[1,2])
