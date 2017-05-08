""" Algorithm:
1. Find a pair for element from A in B, let # of pairs be K
2. If K= N. then maximal is N-1, otherwise K+1
"""

def find_maximal(A, B):
    pairs = 0
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            if A[i] == B[j]:
                pairs += 1
                B.pop(j)
                break
    if pairs == n:
        return pairs - 1
    else:
        return pairs + 1


n = int(raw_input())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
print(find_maximal(a, b))
