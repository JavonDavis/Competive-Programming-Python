#!/bin/python

import sys

largest = 10000000000000000


def f(s, s1, m):
    # print("S1:" + s1)
    if s1[0] == '0':
        return f(s, s1[1:], m - 1) if m - 1 != 0 else largest
    elif s == s1:
        return int(s)
    else:
        if len(s1) > m:
            s2 = s[-2 * m - 1:-len(s1)]
        else:
            s2 = s[-2 * m:-len(s1)]
        if s2 == '':
            s2 = str(0)
        if s2[0] == '0':
            n = f(s, s1, m - 1) if m - 1 != 0 else largest
            p = f(s, s1[1:], m - 1) if m - 1 != 0 else largest
            return min(n, p)
        elif int(s1) - int(s2) == 1:
            n = f(s[:-len(s1)], s2, m)
            p = f(s[:-len(s1)], s2, m - 1) if m - 1 != 0 else largest
            return min(n, p)
        else:
            n = f(s, s1, m - 1) if m - 1 != 0 else largest
            p = f(s, s1[1:], m - 1) if m - 1 != 0 else largest
            return min(n, p)


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here

    if len(s) == 1:
        print "NO"
        continue
    elif len(s) == 2:
        result = s[0] if int(s[1]) - int(s[0]) == 1 else largest
    else:
        result = f(s, s[-(len(s) / 2 + 1):], len(s) / 2 + 1)

    if result != largest:
        print "YES {}".format(result)
    else:
        print "NO"
