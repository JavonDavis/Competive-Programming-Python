def fib_modified(ti, ti1):
    i = 2
    while i < n:
        temp = ti1
        ti1 = ti + pow(ti1, 2)
        ti = temp
        i += 1
    return ti1


t1, t2, n = map(int, raw_input().strip().split())
print fib_modified(t1, t2)
