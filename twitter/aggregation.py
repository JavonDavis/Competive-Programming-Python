# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from heapq import heapify, heappush, heappop


class Node:
    def __init__(self, key, val):  # Each node has a key and a binary heap
        self.key = key
        heap = []
        heapify(heap)
        heappush(heap, val)
        self.heap = heap
        self.left_child = None
        self.right_child = None


class BST:  # Simple BST Data structure
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
        else:
            self.insert_node(self.root, key, val)

    def insert_node(self, currentNode, key, val):
        new_key = key.split('-')
        current_key = currentNode.key.split('-')
        result = cmp(new_key, current_key)
        if result < 0:
            if currentNode.left_child:
                self.insert_node(currentNode.left_child, key, val)
            else:
                currentNode.left_child = Node(key, val)
        elif result > 0:
            if currentNode.right_child:
                self.insert_node(currentNode.right_child, key, val)
            else:
                currentNode.right_child = Node(key, val)
        else:
            heappush(currentNode.heap, val)


def cmp(val1, val2):  # val1 and val2 resembles ('year', 'month')
    y1, m1 = map(int, val1)
    y2, m2 = map(int, val2)
    if y1 < y2:
        return -1
    elif y1 > y2:
        return 1
    else:
        if m1 < m2:
            return -1
        elif m1 > m2:
            return 1
        else:
            return 0


def reverse_inorder(node):  # Reverse inorder traversal of binary tree to print out interactions in sorted order
    if node is None:
        return []
    else:
        return reverse_inorder(node.right_child) + [(node.key, node.heap)] + reverse_inorder(node.left_child)


def count_nodes(node):
    if node is None:
        return 0
    else:
        return 1 + count_nodes(node.left_child) + count_nodes(node.right_child)


date_range = raw_input().strip().split(',')
start_date = date_range[0].strip().split('-')
end_date = date_range[1].strip().split('-')

raw_input()
tree = BST()  # Using simple BST to store the data in sorted order since data more than likely will not be in sorted order but an AVL or RB tree would be a better data structur
while True:  # O(nlgn) time to read in all data points and insert into tree if in range
    data_point = sys.stdin.readline()
    if data_point == '':
        break
    data_point = map(lambda data: data.strip(), data_point.strip().split(','))
    key = data_point[0][:-3]
    if cmp(key.split('-'), start_date) >= 0 and cmp(key.split('-'), end_date) < 0:
        val = (data_point[1], int(data_point[2]))
        tree.insert(key, val)

results = reverse_inorder(tree.root)  # O(n)

for data_result in results:  # O(nmlgm) to read through n dates m interactions for a date in sorted order alphabetically for interactions
    print data_result[0] + ",",
    interactions = data_result[1]
    if len(interactions) == 1:
        print interactions[0][0] + ",", str(interactions[0][1])
        continue
    while interactions:
        current_interaction, total = heappop(interactions)
        if interactions:
            next_interaction, next_value = interactions[0]
            while current_interaction == next_interaction and len(
                    interactions) > 0:  # Handle multiple instances of the same interaction in the month
                heappop(interactions)
                total += next_value
                if interactions:
                    next_interaction, next_value = interactions[0]
            if interactions:
                print current_interaction + ",", str(total) + ",",
            else:
                print current_interaction + ",", str(total)
        else:
            print current_interaction + ",", str(total)
