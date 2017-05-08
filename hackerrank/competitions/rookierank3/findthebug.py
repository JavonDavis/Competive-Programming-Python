#!/bin/python

import sys

def findTheBug(grid):
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            if grid[i][j] == "X":
                return i,j

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)
# Return an array containing [r, c]
result = findTheBug(grid)
print ",".join(map(str, result))
