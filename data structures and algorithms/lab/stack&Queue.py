class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        val = self.top.val
        self.top = self.top.next
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.val

    def get_size(self):
        return self.size

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        val = self.front.val
        self.front = self.front.next
        if self.front is None:   # queue became empty
            self.rear = None
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val

    def get_size(self):
        return self.size

def removeUntil(stack, value):
    curr = stack.top
    while curr.next.val != value:
        temp = curr
        curr = curr.next
        stack.pop(temp)
    stack.pop(curr)
    return stack

def recursiveReverse(queue):
    temp = Stack()
    
    while not queue.is_empty:
        temp.push(queue.peek())
    newqueue = Queue()
    
    while not temp.is_empty:
        newqueue.enqueue(temp.pop())
    
    return newqueue