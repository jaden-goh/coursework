
class binaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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