limit = 100

for i in range(1, limit+1):
    for j in range(1, i+1):
        print i, j


def split_num(num):
    if num % 2 == 0:
        return num - ((num / 2) + 1), num - (num / 2)
    else:
        return num - ((num / 2) + 1), num - ((num / 2) + 1)


def find_max_leaf(tree):
    root = 0
    left = 2*root + 1
    right = 2*root + 2
    while tree[left] != 0 and tree[right] != 0:
        if tree[right] != 0:
            root = right
        else:
            root = left
        left = 2 * right + 1
        right = 2 * right + 2
    return root


# def split(tree):
#     root = find_max_leaf(tree)
#     left = 2 * root + 1
#     right = 2 * root + 2
#     tree[left], tree[right] = split_num(tree[root])
#     return tree[left], tree[right]
#
#
# def run(tree, k):
#     options = (0, 0)
#     while k > 0:
#         k -= 1
#         options = split(tree)
#     return max(options), min(options)
#
#
# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#     n, in_k = [int(s) for s in raw_input().split(" ")]
#     btree = [0 for _ in xrange(2*n)]
#     btree[0] = n
#     max_lr, min_lr = run(btree, in_k)
#     print "Case #{}: {} {}".format(i, max_lr, min_lr)
