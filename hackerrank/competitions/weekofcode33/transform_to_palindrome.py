#!/bin/python

import sys

# def lps(arr):
#     n = len(arr)
#
#     # Create a table to store results of subproblems
#     L = [[0 for x in range(n)] for x in range(n)]
#
#     # Strings of length 1 are palindrome of length 1
#     for i in range(n):
#         L[i][i] = 1
#
#     # Build the table.
#     for cl in range(2, n + 1):
#         for i in range(n - cl + 1):
#             j = i + cl - 1
#             if arr[i] == arr[j] and cl == 2:
#                 L[i][j] = 2
#             elif arr[i] == arr[j]:
#                 L[i][j] = L[i + 1][j - 1] + 2
#             else:
#                 L[i][j] = max(L[i][j - 1], L[i + 1][j])
#
#     return L[0][n - 1]

from collections import defaultdict

n, k, m = raw_input().strip().split(' ')
n, k, m = [int(n), int(k), int(m)]
transformations = defaultdict(set)
for a0 in xrange(k):
    x, y = raw_input().strip().split(' ')
    transformations[int(x)].add(int(y))
    transformations[int(y)].add(int(x))
a = map(int, raw_input().strip().split(' '))


def dfs(start, goal):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex == goal:
            return True
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(transformations[vertex] - visited)
    return False


def path_exists(n1, n2):
    return dfs(n1, n2) or dfs(n2, n1)


def lps(arr):
    n = len(arr)

    # Create a table to store results of subproblems
    dp_table = [[0 for _ in range(n)] for _ in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        dp_table[i][i] = 1

    # Build the table.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if arr[i] == arr[j] or path_exists(arr[i], arr[j]):
                if cl == 2:
                    dp_table[i][j] = 2
                else:
                    dp_table[i][j] = dp_table[i + 1][j - 1] + 2
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i + 1][j])

    return dp_table[0][n - 1]


longest_palindrome = lps(a)
print longest_palindrome


# 10 1 6
# 4 3
# 1 4 5 9 3 1