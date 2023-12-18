class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class LinkedList:
    def __init__(self, head=Node(0), next=None):
        self.head = head
        self.next = next


class HashMap:
    def __init__(self):
        self.map = [LinkedList()]
        self.size = 0

    def hash_code(self, key):
        # compute some algorithm to generate indexes
        index = 0
        return index

    def add(self, key, value):
        self.size += 1

    def remove(self, key):
        self.size -= 1

    def contains(self, key):
        return False

    def size(self):
        return self.size
