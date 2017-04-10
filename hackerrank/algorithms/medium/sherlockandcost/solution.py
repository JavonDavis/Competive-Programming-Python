T = int(raw_input())


def absolute_diff(x, y):
    return abs(x - y)


def g(x, y, b, i, n):
    print x, y, b
    if i == n-1:
        return max(absolute_diff(x, y), absolute_diff(x, 1))
    else:
        num = b[i]
        return max(absolute_diff(x, y) + g(y, num, b), absolute_diff(x, 1) + g(y, 1, b))

def f(b):
    x, y = b[0], b[1]
    num  = b[2]
    return max(absolute_diff(x, 1) + g(1, num, b), absolute_diff(1, y) + g(y, num, b))


for _ in xrange(T):
    N = int(raw_input())
    B = map(int, raw_input().strip().split(' '))
    if N > 1:
        print f(B)
    else:
        print 0
