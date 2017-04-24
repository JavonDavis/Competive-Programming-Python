def is_tidy(x, threshold):
    digit = x % 10
    if digit <= threshold:
        if x < 10:
            return True
        else:
            return is_tidy(x / 10, x % 10)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    last_tidy_number = 0
    count = 1
    while count <= n:
        if is_tidy(count, 9):
            last_tidy_number = count
        count += 1
    print "Case #{}: {}".format(i, last_tidy_number)
