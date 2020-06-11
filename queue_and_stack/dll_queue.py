import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Queue:
    def __init__(self, node=None):
        self.size = 0
        self.head = node
        self.tail = node
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        new_q = ListNode(value)
        self.size += 1

        if self.head is None and self.tail is None:
            self.head = new_q
            self.tail = new_q
        else:
            new_q.prev = self.tail
            self.tail.next = new_q
            self.tail = new_q

    def dequeue(self):
        if self.head is None and self.tail is None:
            pass
        elif self.head == self.tail:
            current_head_value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return current_head_value
        else:
            current_head_value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head = self.head.next
            self.size -= 1
            return current_head_value

    def len(self):
        return self.size
