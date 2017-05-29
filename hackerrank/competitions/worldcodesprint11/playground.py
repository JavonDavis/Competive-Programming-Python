from random import randint

result = ''
for i in range(300000):
    num = randint(0, 8)
    result+=str(num)
# print result
#
# print 100000, 9, 200
k = 100000
print result
num = 1
for c in result:
    if int(c) != 0:
        num = num**(k-1) * int(c)
        num = num %3

print num