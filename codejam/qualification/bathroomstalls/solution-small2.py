def split_num(num):
    if num == 0:
        return 0, 0
    if num % 2 == 0:
        return num - (num / 2), num - ((num / 2) + 1)
    else:
        return num - ((num / 2) + 1), num - ((num / 2) + 1)


def build_graph_ish(n, k):
    nodes = split_num(n)
    while k > 1:
        if k % 2 == 0:
            nodes = split_num(nodes[0])
        else:
            nodes = split_num(nodes[1])
        k /= 2

    return max(nodes), min(nodes)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, in_k = [int(s) for s in raw_input().split(" ")]
    max_lr, min_lr = build_graph_ish(n, in_k)
    print "Case #{}: {} {}".format(i, max_lr, min_lr)
