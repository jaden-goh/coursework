import queues

class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.isEnd = False
        self.next = None
        self.child = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def findchild(self, node, char):
        curr = node.child
        while curr:
            if curr.val == char:
                return curr
            curr = curr.next
        return None            

    def search(self, word):
        curr = self.root
        for char in word:
            node = self.findchild(curr, char)
            if not node:
                return False
            curr = node
        return curr.isEnd
    
    def insert(self, word):
        curr = self.root
        for char in word:
            node = self.findchild(curr, char)
            if node:
                curr = node
            else:
                temp = curr.child
                curr.child = TrieNode(val=char)
                curr.child.next = temp
                curr = curr.child
        curr.isEnd = True
    

    def bfs(self, node):
        Queue = queues
        curr = node
        while curr:
            Queue.enqueue(curr)
            curr = curr.next


    def dfs(node):
        # Pre Order
        print(node.val)
        child = node.child
        while child:
            dfs(child)
            child = child.next
        
    

