N = int(raw_input())

ratings = []
minimas = []

for i in xrange(N):
    ratings.append(int(raw_input()))


def rating(index):
    if index < 0 or index >= N:
        return pow(10, 5) + 1
    return ratings[index]


for i in xrange(N):
    if rating(i - 1) >= rating(i) <= rating(i + 1):
        minimas.append(i)


candies = [0] * N
for minima in minimas:
    candies[minima] = 1

    index = minima - 1
    current_candies = 2
    while index >= 0 and rating(index) > rating(index + 1):
        candies[index] = max(candies[index], current_candies)
        index -= 1
        current_candies += 1

    index = minima + 1
    current_candies = 2
    while index < N and rating(index) > rating(index - 1):
        candies[index] = max(candies[index], current_candies)
        index += 1
        current_candies += 1

print sum(candies)
