class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Hash:
    def __init__(self, num_data):
        self.load_factor = 3
        self.size = max(1, num_data // self.load_factor)
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size


    def hash_search(self, key):
        slot = self.hash(self, key)
        curr = self.table[slot]
        while curr:
            if curr.key == key:
                return True
            else:
                curr = curr.next
        return False
        
    def hash_insert(self, key):
        if self.hash_search(self, key):
            return False
        
        slot = hash(self, key)
        new = Node(key)
        new.next = self.table[slot]
        self.table[slot] = new
        return True
    