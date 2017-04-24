def foo(x):
    if x == 0:
        return 0
    else:
        return foo(x-1)


print foo(pow(10,5))


#!/bin/python

import sys
from collections import defaultdict
from fractions import gcd
from Queue import PriorityQueue

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
nodes = set()
graph = defaultdict(list)

# discovered = set()
dp_table = [[0, 0]]


class Node:
    def __init__(self, val, numer, denom):
        self.val = val
        self.numer = numer
        self.denom = denom

    def __cmp__(self, other):
        current = dp_table[-1]
        return -1 * cmp(float(current[0] + self.numer) / (current[1] + self.denom),
                        float(current[0] + other.numer) / (current[1] + other.denom))


best_traversal = PriorityQueue()
visited = defaultdict(lambda: False)

max_value = -100
# max_numerator = 1
# max_denominator = 100

current_node = None

for a0 in xrange(m):
    u, v, a, b = raw_input().strip().split(' ')
    u, v, a, b = [int(u), int(v), int(a), int(b)]
    if u != v:
        nodes.add(u)
        nodes.add(v)

        # best_traversal.put(Node(v, a, b))
        graph[u].append((v, a, b))
        graph[v].append((u, a, b))

        if float(a) / b >= max_value:
            max_value = float(a) / b
            current_node = u
            # graph[u].append({v:[a,b]})
            # graph[v].append({u:[a,b]})

# print current_node


#
# for current_node in nodes:
#     print "============="
#     best_traversal = PriorityQueue()
#     visited = set()
#     dp_table = [[0, 0]]
#     while visited != nodes:
#         discovered_from_current_node = graph[current_node]
#         visited.add(current_node)
#         for node in discovered_from_current_node:
#             val, numerator, denominator = node
#             best_traversal.put(Node(val, numerator, denominator))
#
#         while not best_traversal.empty():
#             n = best_traversal.get()
#             current_node = n.val
#             if current_node not in visited:
#                 print n.val, n.numer, n.denom
#                 visited.add(current_node)
#                 dp_table.append([n.numer + dp_table[-1][0], n.denom + dp_table[-1][1]])
#                 discovered_from_current_node = graph[current_node]
#                 for node in discovered_from_current_node:
#                     val, numerator, denominator = node
#                     best_traversal.put(Node(val, numerator, denominator))
#     value = float(dp_table[-1][0])/dp_table[-1][1]
#     if value >= max_value:
#         max_value = value
#         max_numerator = dp_table[-1][0]
#         max_denominator = dp_table[-1][1]

# while visited != nodes:
#     n = best_traversal.get()
#     current_node = n.val
#     if current_node not in visited:
#         print n.val, n.numer, n.denom
#         visited.add(current_node)
#         dp_table.append([n.numer + dp_table[-1][0], n.denom + dp_table[-1][1]])

# current_node = graph.keys()[0]
# discovered.add(current_node)

# print graph


while len(visited) != len(nodes):
    discovered_from_current_node = graph[current_node]
    visited[current_node] = True
    for node in discovered_from_current_node:
        val, numerator, denominator = node
        best_traversal.put(Node(val, numerator, denominator))

    while not best_traversal.empty():
        n = best_traversal.get()
        current_node = n.val
        if not visited[current_node]:
            # print n.val, n.numer, n.denom
            visited[current_node] = True
            dp_table.append([n.numer + dp_table[-1][0], n.denom + dp_table[-1][1]])
            discovered_from_current_node = graph[current_node]
            for node in discovered_from_current_node:
                val, numerator, denominator = node
                best_traversal.put(Node(val, numerator, denominator))
                # if n1 not in discovered:
                #     edges = graph[n1]
                #     m_node, m_edge = get_maximal(edges)
                #     print m_edge
                #     new_edge = [m_edge[0] + dp_table[-1][0], m_edge[1] + dp_table[-1][1]]
                #     dp_table.append(new_edge)
                #     discovered.add(n1)
gcd_val = gcd(dp_table[-1][0], dp_table[-1][1])
print "{}/{}".format(dp_table[-1][0] / gcd_val, dp_table[-1][1] / gcd_val)
# gcd_val = gcd(max_numerator, max_denominator)
# print "{}/{}".format(max_numerator/gcd_val, max_denominator/gcd_val)


# Samples
'''
3 3
0 1 1 1
1 2 70 80
2 0 1 2

3 3
0 1 1 1
1 2 70000 80000
2 0 1 2

3 4
0 1 1 9
0 1 2 5
1 2 2 4
2 0 1 2

6 8
0 3 1 1
0 5 1 8
0 4 8 4
5 1 12 3
1 2 6 7
1 4 5 6
4 5 1 8
5 2 2 3

2 1
0 1 1 4

4 5
4 3 6 11
3 2 3 7
2 4 1 5
1 2 1 4
1 3 2 8
'''




# def get_maximal(m_edges):
#     maximal = [0, 0]
#     previous = dp_table[-1]
#     discovered_index = None
#     max_node = None
#     for i in xrange(len(m_edges)):
#         node_item = m_edges[i]
#         node = node_item.keys()[0]
#         a,b = node_item[node]
#         if maximal[1] == 0:
#             maximal = [a,b]
#             max_node = node
#             discovered_index = i
#         else:
#             new_value = float(a+previous[0])/(b+previous[1])
#             maximal_value = float(maximal[0]+previous[0])/(maximal[1]+previous[1])
#             if new_value > maximal_value:
#                 maximal = [a,b]
#                 max_node = node
#                 discovered_index = i
#     m_edges.pop(discovered_index)
#     return max_node, maximal

