#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = -64

for i in xrange(4):
    for j in xrange(4):
        hour_glass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] \
                         + arr[i+2][j+1] + arr[i+2][j+2]
        if hour_glass_sum > max_sum:
            max_sum = hour_glass_sum

print max_sum

