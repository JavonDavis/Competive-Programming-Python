#!/bin/python

import sys


def still_has_burnouts():
    for k in burnout_tracker:
        el = burnout_tracker[k]
        if el[1] == 0:
            return True
    return False


def relax(g, k):
    if k != 0:
        supervisor = supervisors[k]
        burnout_tracker[supervisor][1] = 1
    burnout_tracker[k][1] = 1
    for el in g[k]:
        el[1] = 1

min_val = 0


def dfs(g, i):
    node = g[i]
    global min_val
    if not node:
        if burnout_tracker[i][1]:
            return []
        else:
            return [i]
    else:
        result = []
        for x in node:
            result += dfs(g, x[0])

        if result:
            relax(g, i)
            min_val += 1
            return []
        else:
            if burnout_tracker[i][1]:
                return []
            else:
                return [i]


def dfsi(graph):
    global min_val
    visited, stack = set(), [0]
    vd = [[] for _ in xrange(len(graph))]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            node = set([x[0] for x in graph[vertex]])
            stack.extend(node - visited)
            if vertex != 0:
                vd[supervisors[vertex]].append(burnout_tracker[vertex])
                stack += [supervisors[vertex]]
        else:
            if len(vd[vertex]) != 0 and len(vd[vertex]) == len(graph[vertex]):
                should_relax = False
                for el in vd[vertex]:
                    if el[1] == 0:
                        should_relax = True
                        break
                if should_relax:
                    relax(graph, vertex)
                    min_val += 1
    return visited


def get_leaves(g):
    result = []
    for k in xrange(len(g)):
        if not g[k]:
            result.append(k)
    return result


def dfs_iter(g):
    global min_val
    leaves = get_leaves(g)
    visited = [0 for _ in xrange(len(g))]
    result = [0 for _ in xrange(len(g))]
    children_evaluated = [False for _ in xrange(len(g))]
    for leaf in leaves:
        children_evaluated[leaf] = True
        if burnout_tracker[leaf][1]:
            result[leaf] = 0
        else:
            result[leaf] = 1

    leaves = [supervisors[leaf] for leaf in leaves if leaf != 0]
    while not children_evaluated[0]:
        while leaves:
            k = leaves.pop(0)
            node = g[k]
            all_eval = True
            for el in node:
                if not children_evaluated[el[0]]:
                    all_eval = False
                    break
            if all_eval and not visited[k]:
                visited[k] = 1
                tot = 0
                for el in node:
                    if result[el[0]]:
                        tot = 1
                        break
                if tot > 0:
                    relax(g, k)
                    min_val += 1
                    children_evaluated[k] = True
                    result[k] = 0
                else:
                    if burnout_tracker[k][1]:
                        result[k] = 0
                        children_evaluated[k] = True
                    else:
                        result[k] = 1
                        children_evaluated[k] = True
                if k != 0:
                    leaves.append(supervisors[k])
            else:
                if k != 0:
                    leaves.append(supervisors[k])


#

n = int(raw_input().strip())
# Information for employees 1 through n - 1:
# The first value is the employee's supervisor ID
# The second value is the employee's burnout status (0 is burned out, 1 is not)
graph = [[] for _ in xrange(n)]
burnout_tracker = {0: [0, 1]}
supervisors = {}
for e_i in xrange(1, n):
    e_temp = map(int,raw_input().strip().split(' '))
    supervisors[e_i] = e_temp[0]
    if e_i not in burnout_tracker:
        curr = [e_i, e_temp[1]]
        burnout_tracker[e_i] = curr
    graph[e_temp[0]].append(burnout_tracker[e_i])

# print graph
# print graph[0]
# dfs(graph, 0)
# print min_val
# print dfsi(graph)
dfs_iter(graph)
print min_val
# print min_val
# print still_has_burnouts()
# p = most_burnouts(graph)
# print p
# relax(graph, p)
# print graph
# print still_has_burnouts()

# minimumEmployees = getMinimumEmployees(graph)
# print(minimumEmployees)
