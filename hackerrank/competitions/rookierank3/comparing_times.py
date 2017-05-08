#!/bin/python

import sys

def timeCompare(t1, t2):
    t1 = t1.split(":")
    t2 = t2.split(":")

    decider1 = t1[1][-2:]
    decider2 = t2[1][-2:]
    if decider1 == "AM" and decider2 == "PM":
        return "First"
    elif decider2 == "AM" and decider1 == "PM":
        return "Second"
    else:
        decider1 = int(t1[0])
        decider2 = int(t2[0])
        if decider1 == 12:
            decider1 = 0
        if decider2 == 12:
            decider2 = 0
        if decider1 < decider2:
            return "First"
        elif decider1 > decider2:
            return "Second"
        else:
            decider1 = int(t1[1][:-2])
            decider2 = int(t2[1][:-2])
            if decider1 < decider2:
                return "First"
            else:
                return "Second"

q = int(raw_input().strip())
for a0 in xrange(q):
    t1, t2 = raw_input().strip().split(' ')
    t1, t2 = [str(t1), str(t2)]
    result = timeCompare(t1, t2)
    print(result)
