
def make_optimal_swaps(elements, k):

    index_array = [0 for _ in xrange(len(elements) + 1)]

    for i in xrange(len(elements)):
        index_array[elements[i]] = i

    i = len(elements)
    swaps = 0
    while i > 0 and swaps < k:
        j = len(elements) - i
        if index_array[i] != j:
            temp = index_array[i]
            index_array[i], index_array[elements[j]] = j, index_array[i]
            elements[temp] = elements[j]
            elements[j] = i
            swaps += 1
        i -= 1

    for i in xrange(1, len(index_array)):
        index = index_array[i]
        elements[index] = i
    return elements

n, k = map(int, raw_input().split())
numbers = map(int, raw_input().split())

for el in make_optimal_swaps(numbers, k) : print el,
