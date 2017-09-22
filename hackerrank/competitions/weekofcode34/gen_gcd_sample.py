n = 500000
from random import randint

print n
for _ in xrange(n):
    print randint(1, pow(10, 6)),
print
for _ in xrange(n):
    print randint(1, pow(10, 6)),

