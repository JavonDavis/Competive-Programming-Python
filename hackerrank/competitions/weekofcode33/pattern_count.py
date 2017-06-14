#!/bin/python

import sys

def patternCount(s):
    count = 0
    track = False
    pattern_count = 0
    zero = False
    for el in s:
        if el == '1':
            if not track:
                track = True
            elif zero:
                pattern_count += 1
            count = 0
            zero = False
        elif el == '0':
            if track:
                zero = True
        else:
            track = False
    return pattern_count


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)

