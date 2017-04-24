def calculate_time(distance, speed):
    return float(distance)/speed

def calculate_speed(distance, time):
    return float(distance)/time

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]
    horses = []
    time_for_annie = 0
    for _ in xrange(n):
        ki, si = [int(s) for s in raw_input().split(" ")]
        ti = calculate_time(d-ki, si)
        if ti > time_for_annie:
            time_for_annie = ti
    print "Case #{}: {}".format(i, calculate_speed(d, time_for_annie))
