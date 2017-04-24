'''

Algorithm:
1. Read in important contests
2. Read in unimportant contests
3. Sort important contests in increasing order
4. multiply the first n -k important contests by -1
4. sum luck for both important and unimportant contests
'''

n, k = map(int, raw_input().split())

important = []
not_important = []

for _ in xrange(n):
    li, ti = map(int, raw_input().split())
    if ti == 1:
        important.append(li)
    else:
        not_important.append(li)

important.sort()
for i in range(len(important)-k):
    important[i] *= -1

print sum(important) + sum(not_important)
