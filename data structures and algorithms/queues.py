'''Queues

Properties:
FIFO (First-In, First-Out). Can be array, linked list (this course), or circular buffer.

Functions:

Enqueue: O(1)

Dequeue: O(1)

Peek: O(1)

Variants: Deque (double-ended), Priority Queue (uses heap).

Space: O(n)
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

def is_empty(head):
    if not head.front:
        return True
    else:
        return False

def enqueue(head, node):
    if is_empty(head):
        head.front = node
        head.rear = node
    else:
        head.rear.next = node
        head.rear = node
    head.size += 1

def dequeue(head):
    if is_empty(head):
        raise IndexError("Queue is empty!")
    else:
        curr = head.front
        head.front = head.front.next
        curr.next = None
    
    head.size -= 1
    
    if head.front == None:  
        head.rear = None

    return curr.val 

def getsize(head):
    return head.size

def getfront(head):
    if is_empty(head):
        raise IndexError("Queue is Empty!")
    else:
        return head.front.val

