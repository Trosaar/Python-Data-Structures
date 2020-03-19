import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None # BinarySearchTree
        self.right = None # BinarySearchTree 

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node

        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        # if smaller, go left 
        # if bigger, go right
        # if equal, return True!

        # if smaller, but we cant go left, return false
        # if bigger, but we cant go right, return false
        contained = False

        if target == self.value:
            contained = True
            return contained
        if target < self.value and self.left:
            contained = self.left.contains(target)
        if target > self.value and self.right:
            contained = self.right.contains(target)

        return contained

    # Return the maximum value found in the tree
    def get_max(self):

        max = 0

        if self.right == None:
            max = self.value
            return max
        else:
            max = self.right.get_max()

        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is not None:
            if self.right is not None:
                self.right.for_each(cb)
            if self.left is not None:
                self.left.for_each(cb)
            
            self.value = cb(self.value)

    # DAY 2 Project -----------------------

# Print all the values in order from low to high
# Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
# go left FIRST
        if node.left is not None:
            self.in_order_print(node.left)

# print ourselves
        print(node.value)

# go right 
        if node.right is not None:
            self.in_order_print(node.right)

# Print the value of every node, starting with the given node,
# in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue = Queue(node)

        while self.queue.head is not None:
            self.queue.head.left.enqueue(self.value)
            self.queue.head.right.enqueue(self.value)

            print(self.queue)

# create a queue for nodes
# add current node to queue
# while the queue isnt empty:
# dequeue a node
# print the node
# add its children
#i.e add left (if you can)
# add right (if you can)

# Print the value of every node, starting with the given node,
# in an iterative depth first traversal


    def dft_print(self, node):
        pass
# create a node_stack
# push the current node onto stack
# while we have items on stack

# print the current value and pop it off

# push the right value of the current node if we can

# push the left value of current node if we can


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(5)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)