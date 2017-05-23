def valid(proc):
    look_out = 'H'
    for c in proc:
        if c == '.':
            continue
        elif c == 'H' and look_out == 'H':
            look_out = 'T'
        elif c == 'T' and look_out == 'T':
            look_out = 'H'
        else:
            return False
    return look_out == 'H'

T = int(raw_input())
for _ in xrange(T):
    n = int(raw_input())
    procession = raw_input().strip()
    if valid(procession):
        print "Valid"
    else:
        print "Invalid"
