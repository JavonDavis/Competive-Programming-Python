t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    print "Case #{}: {} {}".format(i, n + m, n * m)