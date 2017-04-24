def find_optimal_path(current, destination, horse):
    if current == destination:
        return 0
    else:
        distance_to_next_city = city_matrix[current][current + 1]
        path1 = pow(10, 15)
        if horse[0] >= distance_to_next_city:
            horse[0] -= distance_to_next_city
            path1 = float(distance_to_next_city)/horse[1] + find_optimal_path(current +1, destination, horse)

        path2 = pow(10, 15)
        if current != 0:
            new_horse = horses[current]
            if new_horse[0] >= distance_to_next_city:
                new_horse[0] -= distance_to_next_city
                path2 = float(distance_to_next_city)/new_horse[1] + find_optimal_path(current +1, destination, new_horse)

        return min(float(path1), float(path2))
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, q = [int(s) for s in raw_input().split(" ")]
    horses = []
    city_matrix = []
    for _ in xrange(n):
        horses.append([int(s) for s in raw_input().split(" ")])

    for _ in xrange(n):
        city_matrix.append([int(s) for s in raw_input().split(" ")])

    raw_input() #GOing from start to end for small

    print "Case #{}: {}".format(i, find_optimal_path(0, n-1, horses[0]))