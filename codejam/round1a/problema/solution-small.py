invisible = ["?"]

def one_letter_in(matrix):
    element = None
    for m_row in matrix:
        for el in m_row:
            if el not in invisible:
                if element:
                    return None
                else:
                    element = el
    return element


def sub_matrix(matrix, n, m):
    return [m_row[:m] for m_row in matrix[:n]]

def cake_full(matrix):
    for m_row in matrix:
        for el in m_row:
            if el == "?":
                return False
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    r, c = [int(s) for s in raw_input().split(" ")]
    cake = []
    for _ in xrange(r):
        cake.append([s for s in list(raw_input())])

    while not cake_full(cake):
        last_bounds = (1,1)
        last_letter = None
        row_bounds = 1
        while row_bounds < r+1:
            column_bounds = 1
            while column_bounds < c+1:
                letter = one_letter_in(sub_matrix(cake, row_bounds, column_bounds))
                if letter:
                    last_letter = letter
                    last_bounds = (row_bounds, column_bounds)
                column_bounds += 1
            row_bounds += 1
        for row in xrange(last_bounds[0]):
            for column in xrange(last_bounds[1]):
                if cake[row][column] == "?":
                    cake[row][column] = last_letter
        invisible.append(last_letter)
    invisible = ["?"]
    print "Case #{}:".format(i)
    for row in cake:
        print ''.join(row)
