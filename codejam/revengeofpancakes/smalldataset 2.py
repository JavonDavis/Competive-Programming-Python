t = int(raw_input())


def flip(string, index_str):
    """Function to flip pancakes from 0 to index"""
    j = index_str
    tmp = ''
    while j >= 0:
        if string[j] == '-':
            tmp += '+'
        else:
            tmp += '-'
        j -= 1
    if index_str + 1 == len(string):
        return tmp
    else:
        return tmp + string[index_str + 1:]


for i in xrange(1, t + 1):
    s = raw_input()
    count = 0
    while '-' in s:
        index = s.rfind('-')
        if s[0] == '-':
            s = flip(s, index)
        else:
            s0 = s[0:index]
            plus_index = s0.rfind('+')
            s = flip(s, plus_index)
        count += 1
    print "Case #{}: {}".format(i, count)
