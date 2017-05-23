#!/bin/python

import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int, raw_input().strip().split(' '))
C = map(int, raw_input().strip().split(' '))
B = []
for B_i in xrange(n):
    B_temp = map(int,raw_input().strip().split(' '))
    B.append(B_temp)
# Write Your Code Here

boxes = [set() for _ in xrange(m)]


def best(i, exclude):
    most_candies = 0
    box = None
    for j in range(len(B[i])):
        if j not in exclude:
            candies = B[i][j]
            if candies > most_candies:
                most_candies = candies
                box = j
    return box, most_candies


def can_put(i, j):
    return i not in boxes[j]


def worth_putting(i, j):
    current_capacity = len(boxes[j])
    proposed_capacity = current_capacity + 1
    if proposed_capacity <= C[j]:
        return True
    candies_earned = B[i][j]
    difference = proposed_capacity - current_capacity
    diff_squared = difference ** 2
    return candies_earned > diff_squared


def put(i, j):
    boxes[j].add(i)


def solve():
    total = 0
    play = True
    penalties = {}
    while play:
        play = False
        for i in xrange(n):
            if A[i] > 0:
                exclude = set()
                for j in xrange(m):
                    if not can_put(i, j):
                        exclude.add(j)
                j, candies = best(i, exclude)
                while len(exclude) != m:
                    if j is None:
                        break
                    if not worth_putting(i, j):
                        exclude.add(j)
                        j, candies = best(i, exclude)
                    else:
                        play = True
                        put(i, j)
                        if len(boxes[j]) > C[j]:
                            penalties[j] = ((len(boxes[j]) - C[j])**2)
                        A[i] -= 1
                        break
                total += candies
    for box in penalties:
        total -= penalties[box]
    return total


print(solve())