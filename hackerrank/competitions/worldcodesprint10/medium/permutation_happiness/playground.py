# #!/bin/python
#
# import sys
# from itertools import permutations
#
def has_k_happy_ids(perm, k):
    happy_count = 0
    c_i = 0
    n = len(perm)

    if n == 1:
        return False
    while c_i < n:
        if c_i == 0:
            if perm[c_i] < perm[c_i + 1]:
                happy_count += 1
        elif c_i == n - 1:
            if perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        else:
            if perm[c_i] < perm[c_i + 1] or perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        c_i += 1
        if happy_count == k:
            return True
    return False


def happy_ids(perm):
    happy_count = 0
    c_i = 0
    n = len(perm)

    if n == 1:
        return 0
    while c_i < n:
        if c_i == 0:
            if perm[c_i] < perm[c_i + 1]:
                happy_count += 1
        elif c_i == n - 1:
            if perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        else:
            if perm[c_i] < perm[c_i + 1] or perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        c_i += 1
    return happy_count


#
#
#
# def query(n, k):
#     modulo = pow(10, 9) + 7
#     ids = range(1, n+1)
#     perms = permutations(ids)
#     # print len(perms)
#     happy_count = 0
#     for perm in perms:
#         if has_k_happy_ids(perm, k):
#             happy_count = (happy_count%modulo + 1)
#     return happy_count%modulo
#
# q = int(raw_input().strip())
# for a0 in xrange(q):
#     n, k = raw_input().strip().split(' ')
#     n, k = [int(n), int(k)]
#     # Find the number of ways to arrange 'n' people such that at least 'k' of them will be happy
#     # The return value must be modulo 10^9 + 7
#     result = query(n, k)
#     print(result)



# n = 5;
# sequence = [ 1, 2, 0, 1, 0 ];
# mlist = [ 'a', 'b', 'c', 'd', 'e']
# permuted = ['' for _ in xrange(n)]
# mset = [False for _ in xrange(n)]
#
# for i in xrange(n):
#     s = sequence[i];
#     remainingPosition = 0;
#
#     # Find the s'th position in the permuted list that has not been set yet.
#     for index in xrange(n):
#         if (not mset[index]):
#             if (remainingPosition == s):
#                 break
#
#             remainingPosition+= 1;
#
#     permuted[index] = mlist[i];
#     mset[index] = True;
#
# print permuted
# print mset

# def perm(n, k):
#     m=k
#     permuted = [0 for _ in xrange(n)]
#     elems = range(n)
#     for i in xrange(n):
#        ind=m%(n-i)
#        m=m/(n-i)
#        permuted[i]=elems[ind]
#        elems[ind]=elems[n-i-1]
#     return permuted;
#
# def inv(perm):
#     k=0
#     m=1
#     n=len(perm);
#     pos = range(n)
#     elems = range(n)
#     for i in xrange(n):
#        k+=m*pos[perm[i]]
#        m=m*(n-i)
#        pos[elems[n-i-1]]=pos[perm[i]]
#        elems[pos[perm[i]]]=elems[n-i-1]
#     return k
#
# count = 0
# for i in xrange(2*pow(10, 14)):
#     if has_k_happy_ids(perm(16, i), 9):
#         count += 1
#
# print count

from math import factorial


def f(N, perm, k):
    if k <= N/2:
        return factorial(N)
    elif k == N-1:
        return pow(2, N-1)
    hids = happy_ids(perm)
    if hids >= k:
        return factorial(N - len(perm))
    elif k - hids > N - len(perm):
        return 0
    # elif k - hids == N - len(perm):
    #     return 0
    # elif k - hids == (N - len(perm) - 1):
    #     return pow(2, k - hids) + 1

    if len(perm) == N:
        return 0
    else:
        return sum(f(N, perm + [i], k) % (pow(10, 9) + 7) for i in xrange(N) if i not in perm) % (pow(10, 9) + 7)
        # total = 0
        # for i in xrange(N):
        #     if i not in perm:
        #         total += f(N, perm + [i], k)
        # return total


print f(7, [], 5)
# def PlainChanges(n):
#     """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
#     if n < 1:
#         return
#     up = xrange(n-1)
#     down = xrange(n-2,-1,-1)
#     recur = PlainChanges(n-1)
#     try:
#         while True:
#             for x in down:
#                 yield x
#             yield next(recur) + 1
#             for x in up:
#                 yield x
#             yield next(recur)
#     except StopIteration:
#         pass
#
# def SteinhausJohnsonTrotter(x):
#     """Generate all permutations of x.
#     If x is a number rather than an iterable, we generate the permutations
#     of range(x)."""
#
#     # set up the permutation and its length
#     try:
#         perm = list(x)
#     except:
#         perm = list(range(x))
#     n = len(perm)
#
#     # run through the sequence of swaps
#     yield perm
#     for x in PlainChanges(n):
#         perm[x],perm[x+1] = perm[x+1],perm[x]
#         yield perm
#
#
# x = list(SteinhausJohnsonTrotter(16))
