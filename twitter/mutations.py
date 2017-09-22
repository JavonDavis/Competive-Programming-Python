# Complete the function below.

def dijkstras(graph, start, goal):
    from heapq import heapify, heappush, heappop
    heap = [(0, start)]
    heapify(heap)
    visited = set()
    while heap:
        cost, genome = heappop(heap)
        if genome == goal:
            return cost
        if genome in visited:
            continue
        visited.add(genome)
        if genome not in graph:
            continue
        for adj in graph[genome]:
            if adj not in visited:
                heappush(heap, (cost + 1, adj))
    return -1


def get_valid_one_mutations(genome, bank):  # O(8 * 4 * ~12) = O(~384) = O(1)
    """
    Get all possible one step mutations for a genome in constant time
    """
    alphabet = ['A', 'C', 'G', 'T']
    valid = set()
    for i in xrange(8):
        for j in xrange(4):
            if genome[i] == alphabet[j]:
                continue
            tmp = genome[:i] + alphabet[j] + genome[i + 1:]
            if tmp in bank:
                valid.add(tmp)
    return valid


def findMutationDistance(start, end,
                         bank):  # I also considered a solution that was exponential in terms of the length of the Sting(=8)
    # Since we were dealing with a fixed length but decided this to be a more appropriate solution
    bank = set(bank)
    graph = {}
    # print start
    edges = get_valid_one_mutations(start, bank)
    if edges:
        graph[start] = edges

    # Build graph in O(n) time
    for genome in bank:
        edges = get_valid_one_mutations(genome, bank)
        if edges:
            graph[genome] = edges
    return dijkstras(graph, start, end)  # O(ElgN)