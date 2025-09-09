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
    while stack.top.val != value:
        stack.pop()
    return stack

def recursiveReverse(queue):
    temp = Stack()
    
    while not queue.is_empty:
        temp.push(queue.peek())
    newqueue = Queue()
    
    while not temp.is_empty():
        newqueue.enqueue(temp.pop())
    
    return newqueue

def palindrome(word):
    front = ""
    back = ""
    stack = Stack()
    for char in word:
        front += char
        stack.push(char)
    while not stack.is_empty():
        back += stack.pop()
    
    return front == back

def balanced(expression):
    map = {"(":")", "[":"]", "{":"}"}
    stack = Stack()
    for char in expression:
        if char in ["(","[","{"]:
            stack.push(char)
        elif char in [")","]","}"]:
            if stack.top:
                if map[stack.top.val] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            return False
    if stack.is_empty():
        return True
    else:
        return False
             

# -----------------------------
# TESTING removeUntil
# -----------------------------
print("\n--- Test removeUntil ---")
s = Stack()
for x in [1, 2, 3, 4, 5]:
    s.push(x)
# Stack is [5,4,3,2,1] with 5 on top
print("Original Stack Top:", s.peek())
s = removeUntil(s, 3)
print("Stack after removeUntil(3):")
while not s.is_empty():
    print(s.pop(), end=" ")
print()

# -----------------------------
# TESTING recursiveReverse
# -----------------------------
print("\n--- Test recursiveReverse ---")
q = Queue()
for x in [1, 2, 3, 4]:
    q.enqueue(x)
# Queue is [1,2,3,4] with 1 at front
print("Original Queue Front:", q.peek())
new_q = recursiveReverse(q)
print("Queue after recursiveReverse:")
while not new_q.is_empty():
    print(new_q.dequeue(), end=" ")
print()

# -----------------------------
# TESTING palindrome
# -----------------------------
print("\n--- Test palindrome ---")
words = ["racecar", "level", "hello", "madam", "stack"]
for w in words:
    print(f"{w}: {palindrome(w)}")


# --------------------------------
# TESTING balanced expression
# --------------------------------

tests = [
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("({[]})", True),
    ("((()))", True),
    ("([{}])", True),
    ("(", False),
    (")", False),
    ("([)]", False),
    ("(([]))", True),
    ("{[()()]}", True),
    ("{[(])}", False),
    ("", True),   # empty string is balanced
]

for expr, expected in tests:
    result = balanced(expr)
    print(f"{expr}: {result} (expected {expected})")
