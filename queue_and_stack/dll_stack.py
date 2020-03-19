import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self, node=None):
        self.size = 0
        self.head = node
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        new_layer = ListNode(value)
        self.size += 1

        if self.head is None:
            self.head = new_layer
        else:
            self.head.prev = new_layer
            new_layer.next = self.head
            self.head = new_layer
            

    def pop(self):
        if self.head is None:
            pass
        elif self.head.next is None and self.head.prev is None:
            top_stack = self.head.value
            self.head = None
            self.size -= 1
            return top_stack

        else:
            top_stack = self.head.value
            next_stack = self.head.next

            self.head.next = None
            next_stack.prev = None
            self.head = next_stack
            self.size -= 1
            
            return top_stack

    def len(self):
        return self.size
