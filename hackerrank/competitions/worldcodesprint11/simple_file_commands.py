#!/bin/python

import sys
import heapq

directory = {}

highest = {}
exists = {}

q = int(raw_input().strip())
# Process each command
for a0 in xrange(q):
    # Read the first string denoting the command type
    command = raw_input().strip().split()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    # print command
    if command[0] == 'crt':
        if command[1] not in directory:
            highest[command[1]] = 1
            directory[command[1]] = []
            exists[command[1]] = True
            print "+ " + command[1]
        else:
            if not directory[command[1]]:
                directory[command[1]] = [highest[command[1]]]
                highest[command[1]] += 1
            lowest = directory[command[1]][0]
            if lowest == 0:
                exists[command[1]] = True
                print "+ " + command[1]
            else:
                name = command[1] + "({})".format(lowest)
                exists[name] = True
                print "+ " + name
            heapq.heappop(directory[command[1]])
    elif command[0] == 'del':
        full = command[1].split("(")
        name = full[0]
        if len(full) > 1:
            num = int(full[1][:-1])
        else:
            num = 0
        # print name
        exists[command[1]] = False
        heapq.heappush(directory[name], num)
        print "- " + command[1]
    else:
        # delete
        full = command[1].split("(")
        name = full[0]
        if len(full) > 1:
            num = int(full[1][:-1])
        else:
            num = 0
        # print name
        exists[command[1]] = False
        heapq.heappush(directory[name], num)

        # Create
        name = ""
        if command[2] not in directory:
            highest[command[2]] = 1
            directory[command[2]] = []
            exists[command[2]] = True
            name = command[2]
        else:
            if not directory[command[2]]:
                directory[command[2]] = [highest[command[2]]]
                highest[command[2]] += 1
            lowest = directory[command[2]][0]
            if lowest == 0:
                exists[command[1]] = True
                name = command[2]
            else:
                name = command[2] + "({})".format(lowest)
                exists[name] = True
            heapq.heappop(directory[command[2]])
        print "r {} -> {}".format(command[1], name)



