def model_value(model):
    if model in ('x', '+'):
        return 1
    elif model == 'o':
        return 2
    else:
        return 0

from copy import deepcopy

class FashionNode:
    def __init__(self, row, column, edges):
        self.row = row
        self.column = column
        self.edges = edges


def explore_fashion(row, column, n, parent, visited, x_allowed_hr=True, x_allowed_dg=True, o_allowed=True,
                    plus_allowed=True):
    options = [(row - 1, column), (row + 1, column), (row + 1, column + 1), (row, column + 1), (row, column - 1),
               (row - 1, column - 1)]


class FashionShow:
    def __init__(self, n, matrix):
        self.n = n
        self.matrix = deepcopy(matrix)

    def __getitem__(self, position):
        return self.matrix[position[0]][position[1]]

    def __setitem__(self, key, value):
        self.insert_model(value, *key)

    def can_insert_model(self, model, row, column):
        if model == '+':
            return self.can_insert_model_plus(row, column)
        elif model == 'x':
            return self.can_insert_model_x(row, column)
        else:
            return self.can_insert_model_o(row, column)

    def can_insert_model_plus(self, row, column):
        # Check right up diagonal
        i, j = row, column
        while i > -1 and j < self.n:
            if self.matrix[i][j] in ('o', '+'):
                return False
            i -= 1
            j += 1

        # Check right down diagonal
        i, j = row, column
        while i < self.n and j < self.n:
            if self.matrix[i][j] in ('o', '+'):
                return False
            i += 1
            j += 1

        # Check left up diagonal
        i, j = row, column
        while i > -1 and j > -1:
            if self.matrix[i][j] in ('o', '+'):
                return False
            i -= 1
            j -= 1

        # Check left down diagonal
        i, j = row, column
        while i < self.n and j > -1:
            if self.matrix[i][j] in ('o', '+'):
                return False
            i += 1
            j -= 1

        return True

    def can_insert_model_x(self, row, column):
        # Check right horizontal
        i, j = row, column
        while j < self.n:
            if self.matrix[i][j] in ('o', 'x'):
                return False
            j += 1

        # Check left horizontal
        i, j = row, column
        while j > -1:
            if self.matrix[i][j] in ('o', 'x'):
                return False
            j -= 1

        # Check vertical up
        i, j = row, column
        while i > -1:
            if self.matrix[i][j] in ('o', 'x'):
                return False
            i -= 1

        # Check vertical down
        i, j = row, column
        while i < self.n:
            if self.matrix[i][j] in ('o', 'x'):
                return False
            i += 1

        return True

    def can_insert_model_o(self, row, column):
        # Check right up diagonal
        i, j = row, column
        while i > -1 and j < self.n :

            if self.matrix[i][j] in ('o', '+'):
                return False
            i -= 1
            j += 1

        # Check right down diagonal
        i, j = row, column
        while i < self.n  and j < self.n :

            if self.matrix[i][j] in ('o', '+'):
                return False
            i += 1
            j += 1

        # Check left up diagonal
        i, j = row, column
        while i > -1 and j > -1:

            if self.matrix[i][j] in ('o', '+'):
                return False
            i -= 1
            j -= 1

                # Check left down diagonal
        i, j = row, column
        while i < self.n  and j > -1:

            if self.matrix[i][j] in ('o', '+'):
                return False
            i += 1
            j -= 1

        # Check right horizontal
        i, j = row, column
        while j < self.n :

            if self.matrix[i][j] in ('o', 'x'):
                return False
            j += 1

        # Check left horizontal
        i, j = row, column
        while j > -1:

            if self.matrix[i][j] in ('o', 'x'):
                return False
            j -= 1

        # Check vertical up
        i, j = row, column
        while i > -1:

            if self.matrix[i][j] in ('o', 'x'):
                return False
            i -= 1

        # Check vertical down
        i, j = row, column
        while i < self.n:
            if self.matrix[i][j] in ('o', 'x'):
                return False
            i += 1

        return True

    def insert_model(self, model, row, column):
        self.matrix[row][column] = model

    def value(self):
        return sum([sum(map(model_value, row)) for row in self.matrix])


def build_show(n, start_configurations):
    lineup = [['.' for _ in xrange(n)] for _ in xrange(n)]
    for config in start_configurations:
        row, column = config[1] - 1, config[2] - 1
        lineup[row][column] = config[0]
    f_show = FashionShow(n, lineup)
    return f_show


def get_most_stylish_lineup(show, n, row, column, max_val, max_show, memory=[]):
    while row < n:
        while column < n:

            if show.can_insert_model_plus(row, column):
                plus_show = FashionShow(n, show.matrix)
                plus_show[(row, column)] = '+'
                value_plus = get_most_stylish_lineup(plus_show, n, row, column + 1, max_val, plus_show, memory)[0]
                if value_plus > max_val:
                    max_val = value_plus
                    memory.append(('+', row, column))
            if show.can_insert_model_o(row, column):
                o_show = FashionShow(n, show.matrix)
                o_show[(row, column)] = 'o'
                value_o = get_most_stylish_lineup(o_show, n, row, column + 1, max_val, o_show, memory)[0]
                if value_o > max_val:
                    max_val = value_o
                    memory.append(('o', row, column))
            if show.can_insert_model_x(row, column):
                x_show = FashionShow(n, show.matrix)
                x_show[(row, column)] = 'x'
                value_x = get_most_stylish_lineup(x_show, n, row, column + 1, max_val, x_show, memory)[0]
                if value_x > max_val:
                    max_val = value_x
                    memory.append(('x', row, column))
            empty_show = FashionShow(n, show.matrix)
            value_empty = get_most_stylish_lineup(empty_show, n, row, column + 1, max_val, show, memory)[0]
            if value_empty > max_val:
                max_val = value_empty
                max_show = show
            column += 1
        row += 1
        column = 0
    return max(show.value(), max_val)


# def get_most_stylish_lineup(show, n):
#     models = []
#
#     show_not_full = False
#
#     while not show_not_full:
#         show_not_full = True
#         for i in xrange(n):
#             for j in xrange(n):
#                 if show.matrix[i][j] != 'o':
#                     if show.can_insert_model_o(i, j):
#                         model = ('o', i, j)
#                         show.insert_model(*model)
#                         models.append(model)
#                         show_not_full = False
#         for i in xrange(n):
#             for j in xrange(n):
#                 if show.matrix[i][j] != '+':
#                     if show.can_insert_model_plus(i, j):
#                         model = ('+', i, j)
#                         show.insert_model(*model)
#                         models.append(model)
#                         show_not_full = False
#         for i in xrange(n):
#             for j in xrange(n):
#                 if show.matrix[i][j] != 'x':
#                     if show.can_insert_model_x(i, j):
#                         model = ('x', i, j)
#                         show.insert_model(*model)
#                         models.append(model)
#                         show_not_full = False
#     return show.value(), models


t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
    N, m = [int(s) for s in raw_input().split(" ")]
    start_config = []
    for m_i in xrange(m):
        mconfig = raw_input().split()
        mconfig[1] = int(mconfig[1])
        mconfig[2] = int(mconfig[2])
        start_config.append(mconfig)
    mem = []
    fashion_show = build_show(N, start_configurations=start_config)
    points, p = get_most_stylish_lineup(fashion_show, N, 0, 0, 0,None, mem)
    models = []
    print p.matrix
    print "Case #{}: {} {}".format(case, points, len(mem))
    for model_i in mem:
        print "{} {} {}".format(*model_i)
