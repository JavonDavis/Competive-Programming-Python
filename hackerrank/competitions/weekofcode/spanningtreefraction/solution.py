#!/bin/python

from fractions import gcd

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

vertices = []
graph = {}

for a0 in xrange(m):
    u, v, a, b = raw_input().strip().split(' ')
    u, v, a, b = [int(u), int(v), int(a), int(b)]
    if u != v:
        vertices.append((u, v, a, b))
        if u not in graph:
            graph[u] = [(u, v, a, b)]
        else:
            graph[u].append((u, v, a, b))

        if v not in graph:
            graph[v] = [(v, u, a, b)]
        else:
            graph[v].append((v, u, a, b))

max_val = -1
max_numerator = 0
max_denominator = 0

dp_table = [[0,0]]

class Node:
    def __init__(self, val1,val2, numer, denom):
        self.val1 = val1
        self.val2 = val2
        self.numer = numer
        self.denom = denom

    def __cmp__(self, other):
        current = dp_table[-1]
        return -1 * cmp(float(current[0] + self.numer) / (current[1] + self.denom),
                        float(current[0] + other.numer) / (current[1] + other.denom))

from Queue import PriorityQueue
# import time
# start_time = time.time()


for vertex in vertices:
    # print vertex
    n1, n2, a1, b1 = vertex
    dp_table = [[a1, b1]]

    visited = set()
    best_traversal = PriorityQueue()
    # discovered_from_vertex = graph[n1] + graph[n2]
    # print graph[n1] + graph[n2]
    map(best_traversal.put, [Node(*x) for x in (graph[n1] + graph[n2])])
    visited.add(n1)
    visited.add(n2)
    while len(visited) < n:
        # print "Visited:"+str(visited)
        tbr = []
        # while best_traversal.empty():
        discovered_vertex = best_traversal.get()
        # print discovered_vertex
        d1, d2, a2, b2 = discovered_vertex.val1, discovered_vertex.val2, discovered_vertex.numer, discovered_vertex.denom
        if d1 not in visited or d2 not in visited:
            best_vertex = discovered_vertex

            visited.add(best_vertex.val1)
            visited.add(best_vertex.val2)
            dp1, dp2 = dp_table[-1]
            dp_table.append([best_vertex.numer+dp1, best_vertex.denom+dp2])
            map(best_traversal.put, [Node(*o) for o in filter(lambda x: x[0] in visited or x[1] in visited, graph[best_vertex.val1] + graph[best_vertex.val2])])
    dp1, dp2 = dp_table[-1]
    dpval = float(dp1)/dp2
    if dpval > max_val:
        max_val = dpval
        max_numerator = dp1
        max_denominator = dp2
    # print dp_table

gcd_val = gcd(max_numerator, max_denominator)
print "{}/{}".format(max_numerator/gcd_val, max_denominator/gcd_val)

# print("--- %s seconds ---" % (time.time() - start_time))
