#!/bin/python

import sys
from fractions import gcd
from math import sqrt

def maximumGcdAndSumBruteForce(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    max_gcd = 0
    max_sum = 0
    for a in A:
        for b in B:
            if max_gcd > b:
                continue
            result = gcd(a, b)
            if result > max_gcd:
                max_gcd = result
                max_sum = a + b
            elif result == max_gcd:
                if a+b > max_sum:
                    max_sum = a + b
    return max_sum

def maximumGcdAndSum(A, B):
    max_sum = 1
    max_gcd = 0

    # print A
    n =len(A)

    arra = [0] * (max(max(A), max(B)) + 1)
    arrb = [0] * (max(max(A), max(B)) + 1)

    maxa = [0] * (max(max(A), max(B)) + 1)
    maxb = [0] * (max(max(A), max(B)) + 1)

    for i in xrange(n):
        ela = A[i]
        elb = B[i]
        arra[ela] += 1
        arrb[elb] += 1
    n = len(arra)
    counta = [0]*len(arra)
    countb = [0] * len(arrb)
    for i in xrange(1, n):
        for j in xrange(i, n, i):
            counta[i] += arra[j]
            if arra[j] >= 1:
                maxa[i] = j
            countb[i] += arrb[j]
            if arrb[j] >= 1:
                maxb[i] = j

    for i in xrange(1, n):
        if counta[i] >= 1 and countb[i] >= 1:
            max_sum = maxa[i] + maxb[i]
    return max_sum


if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    res = maximumGcdAndSum(A, B)
    print res

# print A
#     n =len(A)
#
    # arr = [0]*(max(max(A), max(B))+1)
    # for i in xrange(n):
    #     ela = A[i]
    #     elb = B[i]
    #     arr[ela] += 1
    #     arr[elb] += 1