from random import randint

print 1
import sys

for i in xrange(1000):

    num = randint(0, 1)
    if num == 0:
        sys.stdout.write('-')
    else:
        sys.stdout.write('+')

sys.stdout.write(" "+str(randint(2, 30)))