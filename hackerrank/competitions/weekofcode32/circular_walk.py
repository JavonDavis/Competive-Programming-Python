#!/bin/python

import sys


def walk(start, end, R):

    if start == end:
        return 0

    seconds = 1

    current_left = start
    current_right = start

    left_lim = current_left - R[start]
    right_lim = current_right + R[start]

    farthest_right = left_lim
    farthest_left = right_lim
    while True:
        while current_left >= left_lim:
            index = current_left
            if current_left < 0:
                index += n
                if current_left + n == end:
                    return seconds
            if current_left == end:
                return seconds
            reach_left = current_left - R[index]
            reach_right = current_left + R[index]
            if reach_left < farthest_left:
                farthest_left = reach_left

            if reach_right > farthest_right:
                farthest_right = reach_right
            current_left -= 1
        while current_right <= right_lim:
            if current_right >= n:
                if current_right % n == end:
                    return seconds
            if current_right == end:
                return seconds
            reach_left = current_right - R[current_right % n]
            reach_right = current_right + R[current_right % n]
            if reach_left < farthest_left:
                farthest_left = reach_left

            if reach_right > farthest_right:
                farthest_right = reach_right
            current_right += 1
        left_lim = farthest_left
        right_lim = farthest_right
        seconds += 1
        if left_lim >= current_left and right_lim <= current_right:
            return -1

    return -1


def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    if s == t: # Started at same position
        return 0

    R = [0]*n
    R[0] = r_0
    for i in xrange(1, n):
        R[i] = (R[i-1] * g + seed) % p
    min_dist = walk(s, t, R)
    return min_dist


n, s, t = raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
