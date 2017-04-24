def is_possible(s, k):
    s_i = 0

    count = 0
    while s_i < (len(s) - (k - 1)):  # Note to self, len is constant time
        if s[s_i] == '-':
            for k_i in xrange(k):
                if s[s_i + k_i] == '-':
                    s[s_i + k_i] = '+'
                else:
                    s[s_i + k_i] = '-'
            count += 1
        s_i += 1
    return '-' not in s[-k:], count


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    pancakes, flipper_k = [p for p in raw_input().split(" ")]
    flipper_k = int(flipper_k)

    flip_possible, minimum_moves = is_possible(list(pancakes), flipper_k)
    if not flip_possible:
        minimum_moves = "IMPOSSIBLE"
    print "Case #{}: {}".format(i, minimum_moves)
