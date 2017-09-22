
# from random import choice
# array = [choice([0, 1, -1]) for _ in xrange(8000)]

# O(n^2)
def sumsToZero2(array):
    count = 0
    for i in xrange(len(array)):
        _sum = 0
        arr = []
        for j in xrange(i, len(array)):
            _sum += array[j]
            arr += [array[j]]
            if _sum == 0:
                # print arr
                _sum = 0
                count += 1

    return count


# O(n) time + O(n) extra space
def sumsToPredicate(array, predicate):
    count = 0
    mmap = {}
    initial = [-1]
    mmap[0] = initial
    preSum = 0
    for i in xrange(len(array)):
        preSum += array[i]
        # If point where sum = (preSum - k) is present, it meanst that between that
        # point and this, the sum has to be equal to k

        if predicate(preSum) and preSum in mmap:
            startIndices = mmap[preSum]
            count += len(startIndices)
                # print "{} - {}".format(start + 1, i)

        newStart = []
        if preSum in mmap:
            newStart = mmap[preSum]

        newStart.append(i)
        mmap[preSum] = newStart
    return count

# print sumsToZero(array)
# print sumsToZero2(array)


# Converts an array to an element of 1, 0, -1 where 1 replaces xval, -1 replaces yval and 0 otherwise
def convert(array, xval, yval):
    def converted_value(val):
        if val == xval:
            return 1
        elif val == yval:
            return -1
        else:
            return 0
    return map(converted_value, array)

results = []
from math import factorial
if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = map(int, raw_input().strip().split(' '))
    infinity = (n*(n+1))/2
    keys = set(arr)
    for a0 in xrange(q):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]

        if x not in keys and y not in keys:
            results.append(infinity)
        else:
            converted_array = convert(arr, x, y)
            results.append(sumsToPredicate(converted_array, lambda x: x % 2 == 0 if x == y else lambda x: True))

    for result in results:
        print result
