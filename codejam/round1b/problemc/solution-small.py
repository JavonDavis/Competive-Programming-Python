from copy import copy

def find_optimal_path(current, next, destination, horse0, horse1):
    if current == destination:
        return 0
    else:
        distance_to_next_city = city_matrix[current][next + 1]

        path1 = pow(10, 15)
        if horse0 >= distance_to_next_city:
            path1 = float(distance_to_next_city)/horse1 + find_optimal_path(current + 1, next + 1, destination, horse0 - distance_to_next_city, horse1)

        path2 = pow(10, 15)
        if next != 0:
            k = horses[next][0]
            j = horses[next][1]
            # new_horse = [k,j]
            if k >= distance_to_next_city:
                path2 = float(distance_to_next_city)/j + find_optimal_path(current + 1, next + 1, destination, k - distance_to_next_city, j)


        return min(float(path1), float(path2))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, q = [int(s) for s in raw_input().split(" ")]
    # print n,q
    horses = []
    city_matrix = []
    for _ in xrange(n):
        horses.append([int(s) for s in raw_input().split(" ")])

    for _ in xrange(n):
        city_matrix.append([int(s) for s in raw_input().split(" ")])

    raw_input() #GOing from start to end for small

    print "Case #{}: {}".format(i, find_optimal_path(0,0, n-1, horses[0][0], horses[0][1]))