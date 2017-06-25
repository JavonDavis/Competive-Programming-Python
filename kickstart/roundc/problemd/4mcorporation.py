T = int(raw_input())
from math import ceil

def minimum_departements(minimum, maximum, mean, median):
    if maximum < mean or mean < minimum or mean < median or maximum < median or median < minimum:
        return "IMPOSSIBLE"

    if minimum == maximum:
        return 1

    departments = minimum + maximum
    count = 2
    current_mean = ceil(departments/float(count))

    while current_mean != mean:
        if current_mean > mean:
            departments += minimum
            departments += median
            departments += minimum
        else:
            departments += maximum
            departments += median
            departments += minimum
        count += 1
        current_mean = ceil(departments // float(count))
    return count

for case in xrange(1, T + 1):
    minimum, maximum, mean, median = map(int, raw_input().split())
    print "Case #{}: {}".format(case, minimum_departements(minimum, maximum, mean, median))