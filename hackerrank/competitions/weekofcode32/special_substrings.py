#!/bin/python

import sys


class SuffixTree(object):
    class Node(object):
        def __init__(self, lab):
            self.lab = lab  # label on path leading to this node
            self.out = {}  # outgoing edges; maps characters to nodes

    def __init__(self, s):
        """ Make suffix tree, without suffix links, from s in quadratic time
            and linear space """
        s += '$'
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)  # trie for just longest suf
        # add the rest of the suffixes, from longest to shortest
        for i in xrange(1, len(s)):
            # start at root; we'll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j + 1
                    while k - j < len(lab) and s[k] == lab[k - j]:
                        k += 1
                    if k - j == len(lab):
                        cur = child  # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = lab[k - j], s[k]
                        # create "mid": new node bisecting edge
                        mid = self.Node(lab[:k - j])
                        mid.out[cNew] = self.Node(s[k:])
                        # original child becomes mid's child
                        mid.out[cExist] = child
                        # original child's label is curtailed
                        child.lab = lab[k - j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def followPath(self, s):
        """ Follow path given by s.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, offset) where 'node' is child and
            'offset' is label offset.  If we finish on a node, return (node,
            None). """
        cur = self.root
        i = 0
        while i < len(s):
            c = s[i]
            if c not in cur.out:
                return (None, None)  # fell off at a node
            child = cur.out[s[i]]
            lab = child.lab
            j = i + 1
            while j - i < len(lab) and j < len(s) and s[j] == lab[j - i]:
                j += 1
            if j - i == len(lab):
                cur = child  # exhausted edge
                i = j
            elif j == len(s):
                return (child, j - i)  # exhausted query string in middle of edge
            else:
                return (None, None)  # fell off in the middle of the edge
        return (cur, None)  # exhausted query string at internal node

    def hasSubstring(self, s):
        """ Return true iff s appears as a substring """
        node, off = self.followPath(s)
        return node is not None

    def hasSuffix(self, s):
        """ Return true iff s is a suffix """
        node, off = self.followPath(s)
        if node is None:
            return False  # fell off the tree
        if off is None:
            # finished on top of a node
            return '$' in node.out
        else:
            # finished at offset 'off' within an edge leading to 'node'
            return node.lab[off] == '$'


def is_pal(word):
    return all(word[i] == word[-1*(i+1)] for i in xrange(len(word)//2))

_end = '_end_'


def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

def makePs(s):
    result = []
    i = 1
    while i < len(s) +1:
        result.append(s[:i])
        i += 1
    return result

def palindromes(string, results):
    if len(string) == 0:
        return
    if is_pal(string):
        results.add(string)

    str1 = string[:-1]
    str2 = string[1:]
    str3 = string[1:-1]
    palindromes(str1, results)
    palindromes(str2, results)
    palindromes(str3, results)


def substrings(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            yield string[i:j+1]

# def palindrome_substrings(string):
#     return (i for i in substrings(string) if is_pal(i))

memory = {}
pre_memory = {}
new_memory = {}
no_pals = set()
checked = {}


def palindrome_substrings(string):
    global no_pals
    slen = len(string)
    drones = set()
    if slen <= 1:
        drones.add((string, 0))
        memory[string] = drones
        return memory[string]
    key = string[:-1]
    pals = memory[key]
    drones.add((string[-1], len(string) -1))
    rem = set()
    tba = set()
    for nopal in no_pals:
        rem.add(nopal)
        if type(nopal) == type(string) == type(""):
            if len(nopal) > 0 and len(string) > 0:
                if nopal[0] == string[-1]:
                    if is_pal(nopal + string[-1]):
                        drones.add((nopal + string[-1], len(string) -1))
                    else:
                        tba.add(nopal + string[-1])
                else:
                    tba.add(nopal + string[-1])
    if is_pal(string):
        drones.add((string, len(string) -1))
    else:
        no_pals.add(string)
    for pal in pals:
        if pal[1] == len(string) - 2:
            if pal[0][0] == string[-1]:
                if is_pal(pal[0]+string[-1]):
                    drones.add((pal[0]+string[-1], len(string) -1))
                else:
                    no_pals.add(pal[0]+string[-1])
            else:
                no_pals.add(pal[0] + string[-1])

    no_pals = no_pals - rem
    no_pals = no_pals | tba
    # i = 1
    # sample = ""
    # while i <= slen:
    #     sample = string[-i] + sample
    #     if sample not in memory[key]:
    #         if is_pal(sample):
    #             drones.add(sample)
    #     i += 1
    new_memory[string] = drones
    drones = drones | memory[key]
    memory[string] = drones
    # print memory
    return memory[string]

def prefixes(el):
    pre_set = set()
    if len(el) == 1:
        pre_set.add(el)
        pre_memory[el] = pre_set
        return pre_memory[el]
    # print new_memory
    tbc = new_memory[el]
    key = el[:-1]
    pre_set = pre_memory[key]
    for nel in tbc:
        nel = nel[0]
        while len(nel) > 0:
            if nel not in pre_set:
                pre_set.add(nel)
            nel = nel[:-1]
    pre_memory[el] = pre_set
    return pre_set

def solve(s):

    palindrome_substrings(s)
    # print s,drones
    # prefix_set = set()
    # for el in drones:
    #     prefixes(s, el)
    return len(prefixes(s))

def propertyOfString(s):
    # Complete this function
    # trie = make_trie(s)
    # print trie
    # keys = trie.keys()
    # key = keys[0]
    i = 0
    string = ""
    while i < len(s):
        string += s[i]
        print (solve(string))
        i += 1

    # tree = SuffixTree(s)
    # print tree.root
    # ps = makePs(s)
    # print ps

n = int(raw_input().strip())
s = raw_input().strip()
propertyOfString(s)
# print "\n".join(map(str, result))
# print set(palindrome_substrings(s))
# print memory

