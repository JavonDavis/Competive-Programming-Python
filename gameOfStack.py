#!/bin/python

import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    # your code goes here
    totalSum = 0
    count = 0

    while len(a) != 0 and len(b) != 0:
        el0 = a[0] if len(a) > 0 else -1
        el1 = b[0] if len(b) > 0 else -1
        if el0 != -1 and el1 == -1:
            if totalSum + el0 > x:
                break
            totalSum += el0
            count += 1
            a = a[1:]
        elif el0 == -1 and el1 != -1:
            if totalSum + el1 > x:
                break
            totalSum += el1
            count += 1
            b = b[1:]
        elif el0 == -1 and el1 == -1:
            continue
        else:
            if el0 < el1:
                if totalSum + el0 > x:
                    break
                totalSum += el0
                count += 1
                a = a[1:]
            else:
                if totalSum + el1 > x:
                    break
                totalSum += el1
                count += 1
                b = b[1:]
    print count
