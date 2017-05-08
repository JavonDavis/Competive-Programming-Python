#!/bin/python

import sys
from collections import defaultdict

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
route = []
for route_i in xrange(m):
    route_temp = map(int,raw_input().strip().split(' '))
    route.append(route_temp)

graph = defaultdict(set)

for node in route:
    graph[node[0]].add(node[1])
    graph[node[1]].add(node[0])

visited = set()
count = {}
discovered = []
max_cities = 1

for node in xrange(1, n+1):
    if node not in visited:
        discovered = graph[node]
        visited.add(node)
        curr = 1
        while discovered:
            el = discovered.pop()
            if el not in visited:
                visited.add(el)
                for x in graph[el]:
                    discovered.add(x)
                curr += 1
        if curr > max_cities:
            max_cities = curr

print max_cities
