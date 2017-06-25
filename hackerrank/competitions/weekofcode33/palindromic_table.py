#!/bin/python

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
table = []
table_raw = []
main_digit_count = [0] * 10
for table_i in xrange(n):
    table_temp = map(int, raw_input().strip().split(' '))
    table.append(table_temp)
    for digit in table_temp:
        main_digit_count[digit] += 1


def area(digit_count):
    return sum(digit_count)


def get_digit_count(table_val):
    digit_count = [0] * 10
    for digit in table_val:
        digit_count[digit] += 1
    return digit_count


def can_form_palindrome(digit_count):
    odd_count = 0
    even_elements = []
    odd_elements = []
    for i in range(10):
        if digit_count[i] & 1:
            odd_elements.append(i)
            odd_count += 1
        elif digit_count[i] > 0:
            even_elements.append(i)
    if len(even_elements) == 1 and even_elements[0] == 0:
        if odd_count == 1:
            if digit_count[odd_elements[0]] > 1:
                return True
        return False
    return odd_count <= 1


max_area = 0
count = 0
p, q, r, s = 0, 0, 0, 0
from copy import copy

explored = set()

max_per_level = [0] * 45


def largest_rect(digit_count, row_start, row_end, column_start, column_end, level):
    global max_area, p, q, r, s
    if level == 35:
        return
    if (row_start, row_end, column_start, column_end) in explored:
        return

    if area(digit_count) <= max_area:
        return

    if area(digit_count) <= max_per_level[level]:
        return

    explored.add((row_start, row_end, column_start, column_end))
    if row_start == n:
        return

    if row_end == 0:
        return

    if column_start == m:
        return

    if column_end == 0:
        return

    if can_form_palindrome(digit_count):
        if area(digit_count) > max_area:
            max_area = area(digit_count)
            max_per_level[level] = max_area
            p, q, r, s = row_start, row_end, column_start, column_end
    else:
        a = copy(digit_count)
        i = row_start

        b = copy(digit_count)
        i1 = row_end - 1
        for j in xrange(column_start, column_end):
            a[table[i][j]] -= 1
            b[table[i1][j]] -= 1

        c = copy(digit_count)
        j = column_start
        d = copy(digit_count)
        j1 = column_end - 1
        for i in xrange(row_start, row_end):
            c[table[i][j]] -= 1
            d[table[i][j1]] -= 1

        if can_form_palindrome(a):
            if area(a) > max_area:
                max_area = area(a)
                max_per_level[level] = max_area
                p, q, r, s = row_start + 1, row_end, column_start, column_end

        if can_form_palindrome(b):
            if area(b) > max_area:
                max_area = area(b)
                max_per_level[level] = max_area
                p, q, r, s = row_start, row_end - 1, column_start, column_end

        if can_form_palindrome(c):
            if area(c) > max_area:
                max_area = area(c)
                max_per_level[level] = max_area
                p, q, r, s = row_start, row_end, column_start + 1, column_end

        if can_form_palindrome(d):
            if area(d) > max_area:
                max_area = area(d)
                max_per_level[level] = max_area
                p, q, r, s = row_start, row_end, column_start, column_end - 1

        # if max_area == 0:
        largest_rect(a, row_start + 1, row_end, column_start, column_end, level + 1)
        largest_rect(b, row_start, row_end - 1, column_start, column_end, level + 1)
        largest_rect(c, row_start, row_end, column_start + 1, column_end, level + 1)
        largest_rect(d, row_start, row_end, column_start, column_end - 1, level + 1)


# print(can_form_palindrome("100212"))
# print area("100212")
largest_rect(main_digit_count, 0, n, 0, m, 1)
# if count == 1:
#     print 1/0
print max_area
print p, r, q - 1, s - 1

# 3 4
# 2 3 4 5
# 8 1 1 6
# 9 1 1 7

# 4 4
# 2 3 4 5
# 8 1 1 6
# 9 1 1 7
# 1 2 1 2

# 4 4
# 2 3 4 5
# 8 1 1 6
# 9 1 1 7
# 1 2 1 3