#!/bin/python

import sys

dp_table = [ [0,0,0,0] for _ in xrange(5*pow(10, 5)+1)]

def countSubs(s):
    i = 0
    while i < len(s):
        if s[i] == 'a':
            dp_table[i][0] += 1
        elif s[i] == 'b':
            dp_table[i][1] += 1
        elif s[i] == 'c':
            dp_table[i][2] += 1
        else:
            dp_table[i][3] += 1
        i+= 1
    for i in xrange([[0, 1], [2,3]]):
        for j in xrange(len(dp_table)):
            if dp_table[j][i][0] <= dp_table[j][i][1]:
                
    return (a + c + (a*c)) % (pow(10, 9) + 7)

# Return the number of non-empty perfect subsequences mod 1000000007
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = countSubs(s)
    print(result)
