T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    dp_table = [[0, 0] for _ in xrange(N + 1)]

    arr = map(int, raw_input().strip().split())

    max_contiguous = (pow(10, 4) + 1) * -1
    max_noncontiguous = (pow(10, 4) + 1) * -1
    i = 0
    while i < N:
        if max_noncontiguous < 0:
            if arr[i] > max_noncontiguous:
                max_noncontiguous = arr[i]
        else:
            if arr[i] > 0:
                max_noncontiguous += arr[i]

        dp_table[i][0] = arr[i]
        dp_sum = dp_table[i][0] + dp_table[i][1]
        if dp_table[i][0] > dp_sum:
            dp_table[i+1][1] = dp_table[i][0]
        else:
            dp_table[i+1][1] = dp_table[i][0] + dp_table[i][1]
        if dp_table[i+1][1] >= max_contiguous: #Equality means a 0 was added and the contiguous/non-contiguous sum wouldn't change
            max_contiguous = dp_table[i+1][1]

        i += 1
    print max_contiguous, max_noncontiguous
