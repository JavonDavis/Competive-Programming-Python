#!/bin/python

import sys
from collections import defaultdict



n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

reachable_graph = [set() for _ in xrange(n+1)]
can_reach_graph = [set() for _ in xrange(n+1)]

for a0 in xrange(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    reachable_graph[v].add(u)
    can_reach_graph[u].add(v)
    for city in reachable_graph[u]:
        reachable_graph[v].add(city)
        can_reach_graph[city].add(v)

    for city in can_reach_graph[v]:
        can_reach_graph[u].add(city)
        reachable_graph[city].add(v)

q = int(raw_input().strip())
for a0 in xrange(q):
    x, y, z = raw_input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    # print "Reachable:"+str(reachable_graph)
    # print "Can Reach:"+str(can_reach_graph)
    if x == 1:
        n += 1
        reachable_graph.append(set())
        can_reach_graph.append(set())
        from_node = 0
        to_node = 0
        if z == 0:
            from_node = y
            to_node = n
            # reachable_graph[n].add(y)
            # can_reach_graph[y].add(n)
            # for city in reachable_graph[y]:
            #     reachable_graph[n].add(city)
            #     can_reach_graph[city].add(n)
            #
            # for city in can_reach_graph[n]:
            #     can_reach_graph[y].add(city)
            #     reachable_graph[n].add(city)
        else:
            from_node = n
            to_node = y
            # reachable_graph[y].add(n)
            # can_reach_graph[n].add(y)
            # for city in reachable_graph[n]:
            #     reachable_graph[y].add(city)
            #     can_reach_graph[city].add(y)
            #
            # for city in can_reach_graph[y]:
            #     can_reach_graph[n].add(city)
            #     reachable_graph[y].add(city)
        reachable_graph[to_node].add(from_node)
        can_reach_graph[from_node].add(to_node)
        for city in reachable_graph[from_node]:
            reachable_graph[to_node].add(city)
            can_reach_graph[city].add(to_node)

        for city in can_reach_graph[to_node]:
            can_reach_graph[from_node].add(city)
            reachable_graph[city].add(from_node)
    else:
        if y in reachable_graph[z] or z in can_reach_graph[y]:
            print "Yes"
        else:
            print "No"
