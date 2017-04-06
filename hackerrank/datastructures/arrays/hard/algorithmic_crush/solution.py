#!/bin/python

# Prefix sum scan on a difference array
# Difference array can also be applied to multiple dimensions
n, m = map(int, raw_input().strip().split(' '))

arr = [0 for _ in xrange(n+1)]

for i in xrange(m):
    a, b, k = map(int, raw_input().strip().split(' '))
    arr[a - 1] += k
    arr[b] -= k

max_val = 0
diff = 0

for j in xrange(n):
    diff += arr[j]
    if diff > max_val:
        max_val = diff

print max_val
