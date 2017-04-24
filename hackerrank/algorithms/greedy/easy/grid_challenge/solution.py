# #!/bin/python
# Code would not print out anything accepted by hackerrank
# t = int(input())
#
# def swap(row, i): # i > 0
#     temp = row[i-1]
#     row[i-1] = row[i]
#     row[i] = temp
#
# def has_optimal_solution(grid):
#     for row in grid:
#         min_el = "z"
#         min_i = 0
#         for j in range(len(row)):
#             for i in range(len(row) - j):
#                 el = row[i]
#                 if el <= min_el:
#                     min_el = el
#                     min_i = i
#             while min_i > j:
#                 swap(row, min_i)
#                 min_i -= 1
#             min_el ="z"
#     for i in range(len(grid) - 1):
#         for j in range(len(grid[i])):
#             if grid[i][j] > grid[i + 1][j]:
#                 return False
#     return True
#
# k = []
# for _ in range(t):
#     n = int(input())
#     grid = []
#     for row in range(n):
#         grid.append(list(input()))
#     if has_optimal_solution(grid):
#         k.append("YES")
#     else:
#         k.append("NO")
#
# for i in range(len(k)):
#     print (k[i])

a = [[list(input().strip()) for _ in range(int(input()))] for _ in range(int(input()))]
for i in a:
    i = list(map(sorted, i))
    i = [[i[x][y] <= i[x + 1][y] for x in range(len(i) - 1)] for y in range(len(i))]
    i = all([all(i[m]) for m in range(len(i))])
    print('YES' if i == True else 'NO')
