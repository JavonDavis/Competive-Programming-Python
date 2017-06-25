T = int(raw_input())


def max_score(friends, scores, me, q):
    highest = 0
    for i in xrange(len(friends)):
        friend = friends[i]
        correct = scores[i]
        wrong = q - correct
        my_score = 0
        for j in xrange(len(friend)):
            if wrong and friend[j] != me[j]:
                my_score += 1
                wrong -= 1
            elif correct and friend[j] == me[j]:
                my_score += 1
                correct -= 1
        if my_score > highest:
            highest = my_score
    return highest


for case in xrange(1, T + 1):
    friends = []
    n, q = map(int, raw_input().split())
    for _ in xrange(n):
        friends.append(raw_input())
    me = raw_input()
    scores = map(int, raw_input().split())
    print "Case #{}: {}".format(case, max_score(friends, scores, me, q))