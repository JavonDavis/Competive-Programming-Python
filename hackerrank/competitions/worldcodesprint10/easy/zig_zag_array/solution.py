#!/bin/python

import sys

def increasing(lst, i, j, k):
    return lst[i] < lst[j] < lst[k]

def decreasing(lst, i, j, k):
    return lst[i] > lst[j] > lst[k]

def minimumDeletions(a):
    if len(a) < 3:
        return 0

    i = 0
    middle = 1
    end = 2
    remove_count = 0

    while end < len(a):
        if increasing(a, i, middle, end):
            remove_count += 1
            middle = end
            end += 1
        elif decreasing(a, i, middle, end):
            remove_count += 1
            middle = end
            end += 1
        else:
            i = middle
            middle = end
            end += 1
    return remove_count


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)
