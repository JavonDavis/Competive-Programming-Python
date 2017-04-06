#!/bin/python

n, q = map(int, raw_input().strip().split(' '))
last_ans = 0
seqLst = [[0] for seq_i in xrange(n)]


def f(x): return (x ^ last_ans) % n


for i in xrange(q):
    q_type, x_val, y_val = map(int, raw_input().strip().split(' '))
    if q_type == 1:
        seq = seqLst[f(x_val)]
        seq[0] += 1
        seq.append(y_val)
    else:
        seq = seqLst[f(x_val)]
        seq_size = seq[0]
        element_index = (y_val % seq_size) + 1
        last_ans = seq[element_index]
        print last_ans

