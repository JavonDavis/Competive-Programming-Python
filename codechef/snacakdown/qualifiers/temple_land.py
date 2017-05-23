def valid(strip, n):
    if n %2 == 0:
        return False
    return sum(strip) == strip[n/2]**2

T = int(raw_input())
for _ in xrange(T):
    n = int(raw_input())
    strip = map(int, raw_input().strip().split())
    if valid(strip, n):
        print "yes"
    else:
        print "no"
