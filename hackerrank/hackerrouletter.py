#!/bin/python

import sys


def calc_sum(a, n, m):
    return (((calc_power(a, n, m) - 1) % m) / a % m) % m


def calc_sum2(a, n):
    return (pow(a + 1, n) - 1) / a


def calc_power(a, n, m):
    return pow(a + 1, n, m)

def calculate_position(a,b, n):
    return pow(a + 1, n) * x + calc_sum2(a, n) * b


def find_number_of_kicks_for_one_complete_go_around(a, x, m):
    initial = x
    i = 1
    position = calculate_position(a, b, i)

    while position != initial:
        print "Position", position
        i += 1
        position = calculate_position(a, b, i)

    return i, position%m


"""
geometricSeriesMod[a_, n_, m_] := 
   Module[ {q = a, exp = n, factor = 1, sum = 0, temp},

   While[And[exp > 0, q != 0],
     If[EvenQ[exp],
       temp = Mod[factor*PowerMod[q, exp, m], m];
       sum = Mod[sum + temp, m];
       exp--];
     factor = Mod[Mod[1 + q, m]*factor, m];
     q = Mod[q*q, m];
     exp = Floor[ exp /2];
   ];

   Return [Mod[sum + factor, m]]
]

"""

def geometricSeriesMod(a,n,m):
    q = a
    exp = n
    factor = 1
    total = 0
    while exp > 0 and q != 0:
        if exp & 1 == 0:
            temp = factor * pow(q, exp, m)%m
            total = (total +temp)%m
            total %= m
            exp -= 1
        factor = (((1 + q) %m)* factor)%m
        q = (q%m * q%m ) %m
        exp = exp /2
    return (total%m + factor %m)%m

if __name__ == "__main__":
    x, a, b, m = raw_input().strip().split(' ')
    x, a, b, m = [int(x), int(a), int(b), int(m)]
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())

        # result2 = pow(a + 1, n) * x + calc_sum2(a, n) * b
        # result2 %= m
        # print "Correct", result2
        #
        # kicks, new_start = find_number_of_kicks_for_one_complete_go_around(a, x, m)
        # start = x
        # print kicks, new_start
        # if n >= kicks:
        #     start = new_start
        #     n %= kicks
        # print start, n
        # result = pow(a + 1, n) * start + calc_sum2(a, n) * b
        # print result
        # var1 = a + 1
        # var2 = var1
        # # print var1, var2
        # result = (pow(var1, n, m) * x) + (pow(var2, n, m) - 1)/a * b
        # result = int(result)
        # result %= m
        # print result
        # six = pow(10, 6)
        # seven = pow(10, 7)
        # eight = pow(10, 8)
        # nine = pow(10, 9)
        # if n >= nine:
        #     n %= nine
        # elif n >= eight:
        #     n %= eight
        # if n >= seven:
        #     n %= seven
        # elif n >= six:
        #     n %= six
        #
        result2 = (pow(a + 1, n, m) * x%m)%m + (geometricSeriesMod(a + 1,n - 1,m) * b%m)%m
        result2 %= m
        print result2

        # # !/bin/python
        #
        # import sys
        #
        # if __name__ == "__main__":
        #     x, a, b, m = raw_input().strip().split(' ')
        #     x, a, b, m = [int(x), int(a), int(b), int(m)]
        #     q = int(raw_input().strip())
        #     for a0 in xrange(q):
        #         n = int(raw_input().strip())
        #         start = x
        #         for _ in xrange(n):
        #             start += ((a % m * start % m) % m + b % m) % m
        #         print start % m

                # 1 1000000000 3 10000
# 1
# 1000000000000
#
# 1 4 3 10000
# 1
# 2

# 1 4 3 100
# 1
# 2