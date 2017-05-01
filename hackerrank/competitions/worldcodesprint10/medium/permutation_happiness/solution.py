from math import factorial


def happy_ids(perm):
    happy_count = 0
    c_i = 0
    n = len(perm)

    if n == 1:
        return 0
    while c_i < n:
        if c_i == 0:
            if perm[c_i] < perm[c_i + 1]:
                happy_count += 1
        elif c_i == n - 1:
            if perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        else:
            if perm[c_i] < perm[c_i + 1] or perm[c_i] < perm[c_i - 1]:
                happy_count += 1
        c_i += 1
    return happy_count

factorial_memory = {}


# def f(N, perm, k):
#     hids = happy_ids(perm)
#     if hids >= k:
#         el = N - len(perm)
#         if el not in factorial_memory:
#             factorial_memory[el] = factorial(el)
#         return factorial_memory[el]
#     elif k - hids > N - len(perm):
#         return 0
#     elif k - hids <= (N - len(perm))/2:
#         el = N - len(perm)
#         if el not in factorial_memory:
#             factorial_memory[el] = factorial(el)
#         return factorial_memory[el]
#     if len(perm) == N:
#         return 0
#     else:
#         return sum(f(N, perm + [i], k) % (pow(10, 9) + 7) for i in xrange(N) if i not in perm) % (pow(10, 9) + 7)


def query(n, k):
    if n == k:
        return 0
    elif:
        pass
    else:
        return n*query(n-1, k) + 2*(n-k)*(query(n-1, k-1) - query(n-1, k))

q = int(raw_input().strip())
for a0 in xrange(q):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    # Find the number of ways to arrange 'n' people such that at least 'k' of them will be happy
    # The return value must be modulo 10^9 + 7
    result = query(n, k)
    print(result)
