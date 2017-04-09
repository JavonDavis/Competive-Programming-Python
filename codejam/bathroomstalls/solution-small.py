

def split_num(num):
    if num % 2 == 0:
        return num - ((num / 2) + 1), num - (num / 2)
    else:
        return num - ((num / 2) + 1), num - ((num / 2) + 1)


def run(stall_choices, k):
    options = (0, 0)
    while k > 0:
        k -= 1
        choice = max(stall_choices)
        stall_choices.remove(choice)
        options = split_num(choice)
        stall_choices.extend(options)
    return max(options), min(options)



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, in_k = [int(s) for s in raw_input().split(" ")]
    max_lr, min_lr = run([n], in_k)
    print "Case #{}: {} {}".format(i, max_lr, min_lr)
