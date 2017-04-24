T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    B = map(int, raw_input().strip().split(' '))
    dp_table = [[0, 0] for _ in xrange(N)]
    for i in xrange(N-1):
        dp_table[i+1][0] = max(dp_table[i][0], dp_table[i][1] + abs(B[i] - 1))
        dp_table[i+1][1] = max(dp_table[i][0] + abs(B[i + 1] - 1), dp_table[i][1] + abs(B[i + 1] - B[i]))
    print max(dp_table[N-1][0], dp_table[N-1][1])