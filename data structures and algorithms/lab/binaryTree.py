from stackQueue import Stack, Queue

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

def mirrorTree(node: binaryTreeNode):
    temp = node.left
    node.left = node.right
    node.right = temp
    
    if node.left:
        mirrorTree(node.left)
    
    if node.right:
        mirrorTree(node.right)

    return node

def printSmallerValues(node: binaryTreeNode, m: int):
    if not node:
        return -1
    else:
        if node.key < m:
            print(node.key)
        if node.left:
            printSmallerValues(node.left, m)
        if node.right:
            printSmallerValues(node.right, m)
        
        return

def smallestValue(node: binaryTreeNode):
    if not node:
        return float('inf')
    
    minV = min(node.key, smallestValue(node.left), smallestValue(node.right))
    return minV


def hasGreatGrandchildren(node: binaryTreeNode):
    if not node:
        return -1
    
    gen = 1 + max(hasGreatGrandchildren(node.left), hasGreatGrandchildren(node.right))
    
    if gen >= 3:
        print(node.key)

    return gen    



# ================= TEST =================

def build_balanced_1_to_7():
    #        4
    #      /   \
    #     2     6
    #    / \   / \
    #   1  3  5  7
    n1 = binaryTreeNode(1); n3 = binaryTreeNode(3)
    n5 = binaryTreeNode(5); n7 = binaryTreeNode(7)
    n2 = binaryTreeNode(2); n2.left, n2.right = n1, n3
    n6 = binaryTreeNode(6); n6.left, n6.right = n5, n7
    root = binaryTreeNode(4); root.left, root.right = n2, n6
    return root

def build_right_chain(n=5):
    # 1 -> 2 -> 3 -> ... -> n (all to the right)
    head = None
    for x in range(n, 0, -1):
        node = binaryTreeNode(x)
        node.right = head
        head = node
    return head

if __name__ == "__main__":
    print("\n=== Balanced Tree (1..7) ===")
    root = build_balanced_1_to_7()

    print("\npreOrderTraversal (expected: 4 2 1 3 6 5 7)")
    try:
        preOrderTraversal(root)   # NOTE: your current code recurses left twice; expect wrong output
    except Exception as e:
        print("preOrderTraversal raised:", type(e).__name__, e)

    print("\ninOrderTraversal (expected: 1 2 3 4 5 6 7)")
    try:
        inOrderTraversal(root)
    except Exception as e:
        print("inOrderTraversal raised:", type(e).__name__, e)

    print("\npostOrderTraversal (expected: 1 3 2 5 7 6 4)")
    try:
        postOrderTraversal(root)  # NOTE: your current code self-recurses -> RecursionError
    except Exception as e:
        print("postOrderTraversal raised:", type(e).__name__, e)

    print("\nBFS level order (expected: 4 2 6 1 3 5 7)")
    try:
        breadthFirstSearch(root)  # NOTE: uses Queue.is_empty(); ensure your Queue API matches
    except Exception as e:
        print("breadthFirstSearch raised:", type(e).__name__, e)

    print("\ncountNode, treeHeight (expected: 7, 2)")
    try:
        print("countNode:", countNode(root))
        print("treeHeight:", treeHeight(root))  # height in edges: leaf=0, root here=2
    except Exception as e:
        print("countNode/treeHeight raised:", type(e).__name__, e)

    print("\nmirrorTree once (then inorder should be reversed: 7 6 5 4 3 2 1)")
    try:
        mirrorTree(root)
        inOrderTraversal(root)
    except Exception as e:
        print("mirrorTree/inOrderTraversal raised:", type(e).__name__, e)

    print("\nmirrorTree twice (restore), inorder should be: 1 2 3 4 5 6 7")
    try:
        mirrorTree(root)
        inOrderTraversal(root)
    except Exception as e:
        print("mirrorTree/inOrderTraversal raised:", type(e).__name__, e)

    print("\nprintSmallerValues(<m=4>) (expected: 1 2 3, any order consistent with traversal)")
    try:
        printSmallerValues(root, 4)  
    except Exception as e:
        print("printSmallerValues raised:", type(e).__name__, e)

    print("\nsmallestValue (expected: 1)")
    try:
        print("smallestValue:", smallestValue(root))
    except Exception as e:
        print("smallestValue raised:", type(e).__name__, e)

    print("\nhasGreatGrandchildren on balanced tree (expected: prints nothing; no node has depth>=3)")
    try:
        hasGreatGrandchildren(root)   # NOTE: prints node.val (bug); your nodes use .key
        print("\n(returned:", hasGreatGrandchildren(root), ")")  # will return max depth (edges)
    except Exception as e:
        print("hasGreatGrandchildren raised:", type(e).__name__, e)

    print("\n=== Deep Right Chain (1..5) ===")
    chain = build_right_chain(5)
    print("treeHeight(chain) expected: 4")
    try:
        print("treeHeight:", treeHeight(chain))
    except Exception as e:
        print("treeHeight raised:", type(e).__name__, e)

    print("\nhasGreatGrandchildren(chain) expected: should print nodes with subtree depth >=3 "\
          "(i.e., keys 1 and 2)")
    try:
        hasGreatGrandchildren(chain)
    except Exception as e:
        print("hasGreatGrandchildren raised:", type(e).__name__, e)

    print("\Test End.")
