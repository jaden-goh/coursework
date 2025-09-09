# 1 on Ipad

from stackQueue import Queue

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class binaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, node):
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.val

    def get_size(self):
        return self.size

class binaryTree:
    def __init__(self):
        self.root = None

    # [root, left, right] pre order: starts from root, travels all the way left bottom then makes its way to right bottom, left priority
def preOrderTraversal(node: binaryTreeNode):
    print(node.key)
    if node.left:
        preOrderTraversal(node.left)
    if node.right:
        preOrderTraversal(node.left)
    return

    # [left, root, right] in order, goes all the way left then goes up and checks the direct parent then checks the right
def inOrderTraversal(node: binaryTreeNode):
    if node:
        inOrderTraversal(node.left)
        print(node.key)
        inOrderTraversal(node.right)
    return
    
    # [left, right, root] post order: parent only visited after all children visited, goes all the way down left, then right, then parent
def postOrderTraversal(node: binaryTreeNode):
    if node:
        postOrderTraversal(node)
        postOrderTraversal(node)
        print(node.key)
    return

def breadthFirstSearch(root: binaryTreeNode):
    if not root:
        return -1   
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        curr = queue.dequeue()
        if curr.left:
            queue.enqueue(curr.left)
        if curr.right:
            queue.enqueue(curr.right)

def countNode(root: binaryTreeNode):
    if not root:
        return 0
    return 1 + countNode(root.left) + countNode(root.right)
    
def treeHeight(root: binaryTreeNode):
    if not root:
        return -1
    
    left = treeHeight(root.left)
    right = treeHeight(root.right)

    return 1 + max(left, right)

def levelOrderIterative(root: binaryTreeNode):
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        temp = queue.dequeue()
        if temp.left:
            queue.enqueue(temp.left)
        if temp.right:
            queue.enqueue(temp.right)
        print(temp.key)

    return 

def preOrderIterative(root: binaryTreeNode):
    stack = Stack()
    if root:
        stack.push(root)

    while not stack.is_empty():
        temp = stack.pop()
        
        if temp.right:
            stack.push(temp.right)
        if temp.left:
            stack.push(temp.left)

        print(temp.key)

    return

# height in links, not nodes
def maxDepth(node: binaryTreeNode):
    if not node:
        return -1 #return 0 here if counting nodes instead of links

    depth = 1 + max(maxDepth(node.left), maxDepth(node.right))
    return depth