

def has_moves(string):
    i = 1
    while i < len(string)-1:
        if string[i-1] == '0' and string[i+1] == '0':
            return True
        i += 1
    return False

from copy import copy


def get_moves(string):
    i = 1
    moves = []
    while i < len(string) - 1:
        if string[i - 1] == '0' and string[i + 1] == '0':
            temp = copy(string)
            temp.pop(i)
            moves.append(temp)
        i += 1
    return moves

memory = {}


# def play(config):
#     if len(config) < 3:
#         return 0
#     elif len(config) == 3:
#         if has_moves(config):
#             return 1
#         else:
#             return 0
#     else:
#         moves = get_moves(config)
#         if len(moves) == 0:
#             return 0
#         else:
#             results = []
#             for move in moves:
#                 if move in memory:
#                     results.append(memory[move])
#                 else:
#                     memory[move] = play(move)
#                     results.append(memory[move])
#             return 1 + max(results)

def nextMove(string):
    i = 1
    moves = []
    while i < len(string) - 1:
        if string[i - 1] == '0' and string[i + 1] == '0':
            return i
        i += 1
    return -1


def play(config):
    count = 0
    i = 0
    start = 0
    while i< len(config):
        if config[i] == '0':
            start = i
            break
        i += 1
    i = start + 1
    while i < len(config) - 1:
        if config[start] == '0' and config[i+1] == '0':
            count += 1
            i += 1
        elif config[start] == '0' and config[i+1] == '1':
            start = i
            i = start +1
        else:
            i+= 1
    return count

# def play3(string):
#     alice_start = True
#     i = 1
#     count = 0
#     if len(string) < 3:
#         return alice_start, 0
#     while i < len(string)-1:
#         if string[i-1] == '0' and string[i+1] == '0':
#             if string[i] == '0':
#                 count += 1
#             else:
#                 if count > 0:
#                     count += 1
#                 alice_start = False
#         i += 1
#     return alice_start,count


g = int(raw_input())

def does_alice_win(lst):


    if len(lst) < 3:
        return False

    i = 1
    one_count = 0
    zero_count = 0
    while i < (len(lst) - 1):
        if lst[i-1] == '0' and lst[i+1] == '0':
            if lst[i] == '1':
                lst.pop(i)
                one_count += 1
        i += 1

    i = 1
    while i < (len(lst) - 1):
        if lst[i-1] == '0' and lst[i+1] == '0':
            if lst[i] == '0':
                zero_count += 1
        i += 1

    alice_starts = True

    if one_count %2 == 1:
        alice_starts = False

    if alice_starts:
        if zero_count %2 == 1:
            return True
        else:
            return False
    else:
        if zero_count %2 == 1:
            return False
        else:
            return True

for _ in xrange(g):
    n = int(raw_input())
    game = raw_input().strip().split()
    alice_wins = does_alice_win(game)
    if alice_wins:
        print "Alice"
    else:
        print "Bob"
