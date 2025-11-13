class Hash:
    def __init__(self, num_data):
        self.load_factor = 3
        self.size = max(1, num_data // self.load_factor)
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size
    
    def hash_search(self, key):
        slot = self.hash(key)
        curr = slot
        while not self.table[curr] == key:
            curr += 1
            if curr == self.size - 1:
                curr = 0
            if curr == slot:
                return False
        return curr
        
    def hash_insert(self, key):
        slot = self.hash(key)
        curr = slot
        while self.table[curr] is not None:
            curr += 1
            if curr == self.size:
                curr = 0
        self.table[curr] = key
        return True
    
    def hash_delete(self, key):
        slot = self.hash(key)
        curr = slot
        while not self.table[curr] == key:
            curr += 1
        self.table[curr] == None

