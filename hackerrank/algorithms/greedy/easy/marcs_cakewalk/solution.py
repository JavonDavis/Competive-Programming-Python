#!/bin/python

import sys

def optimal_miles(calories): # Assumes calories is sorted
    j = 0
    i = 0
    miles = 0
    while i < len(calories):
        miles += (pow(2, j) * calories[i])
        i += 1
        j += 1
    return miles

n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
calories.sort(reverse=True)
print(optimal_miles(calories))
