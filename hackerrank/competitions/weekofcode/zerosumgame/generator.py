print 1

num = pow(10, 5)
print num
from random import randint
for i in xrange(0,num):
    print randint(0,1),

def gen(number):
    lst = []
    for i in xrange(0, number):
        lst.append(randint(0, 1))
    return lst