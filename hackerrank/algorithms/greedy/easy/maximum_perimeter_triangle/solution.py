n = int(raw_input())
sticks = sorted(map(int, raw_input().split()))

i = n-3
while i > -1 and (sticks[i] + sticks[i+1] <= sticks[i+2]):
    i -=1

if i > -1:
    print sticks[i], sticks[i+1], sticks[i+2]
else:
    print -1
