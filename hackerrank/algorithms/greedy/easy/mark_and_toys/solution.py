n, k = map(int, raw_input().split())
prices = map(int, raw_input().split())

prices.sort()

count = 0
i = 0
while k - prices[i] > 0:
    k -= prices[i]
    count += 1
    i += 1

print count
