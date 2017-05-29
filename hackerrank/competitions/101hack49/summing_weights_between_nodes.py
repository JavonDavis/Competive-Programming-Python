#!/bin/python

import sys

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' ')) 

graph = [set() for _ in xrange(n+1)]
weights = {}
for a0 in xrange(n-1):
    u, v, w = raw_input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    graph[u].add(v)
    graph[v].add(u)
    weights[(u, v)] = w
    weights[(v, u)] = w

def r_nodes():
    result = []
    for i in xrange(len(c)):
        if c[i] == 0:
            result.append(i + 1)
    return result

def solve():
    total_weight = [0]

    def bfs_paths(start):
        queue = [(start, [start], 0)]
        while queue:
            (vertex, path, weight) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if c[next - 1] == 1:
                    total_weight[0] += (weight + weights[(vertex, next)])
                queue.append((next, path +[next], weight + weights[(vertex, next)]))

    red_nodes = r_nodes()
    for node in red_nodes:
        bfs_paths(node)
    return total_weight[0]

print solve()
