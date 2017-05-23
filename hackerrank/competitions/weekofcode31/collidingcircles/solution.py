#!/bin/python

import sys
from itertools import combinations
from math import pi, pow

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
r = map(int, raw_input().strip().split(' '))

memory = {}
dp_table = [[r]]

#
# def collide(radii, p):
#     if p == 0:
#         return reduce(lambda x,y: x+y, map(lambda x: pi*pow(x,2), radii))
#     else:
#         pairs = list(combinations(radii, 2))
#
#         new_radii = set()
#         for pair in pairs:
#             pair = list(pair)
#             pair_sum = sum(pair)
#             tba = []
#             for el in radii:
#             new_radii.add(tuple([el for el in radii if el not in pair or pair.remove(el)] + [pair_sum]))
#         results = []
#         for mradii in new_radii:
#             if mradii in memory:
#                 results.append(memory[mradii + (p-1,)])
#             else:
#                 memory[mradii+(p-1, )] = collide(mradii, p - 1)
#                 results.append(memory[mradii+(p-1, )])
#         return sum(results)/len(results)
#

# def collide_iter(p):
#     while p > 0:
#         new_radii = set()
#         for entry in dp_table[-1]:
#             pairs = list(combinations(entry, 2))
#             for pair in pairs:
#                 pair = list(pair)
#                 pair_sum = sum(pair)
#                 new_radii.add(tuple([el for el in entry if el not in pair or pair.remove(el)] + [pair_sum]))
#         dp_table.append(list(new_radii))
#         p -=1
#     results = [map(lambda x: pi*pow(x,2), pair) for pair in dp_table[-1]]
#     reductions = [reduce(lambda x,y: x+y, result) for result in results]
#     return sum(reductions)/len(reductions)
# print '%.10f' % collide(r, k)
# print '%.10f' % collide_iter(k)
