class doubleListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f"Value: {self.val}"
    
def displayNodes(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    print(None)

def searchNode(head, index):
    if not head:
        print(None)
    else:
        curr = head
        for i in range(index):
            if not curr:
                break
            else:
                curr = curr.next
        if curr:
            print(curr.val)
        else: 
            print("Index out of range")

def addNode(head,node,index):
    curr = head
    if not head:
        head = node
        return head
    elif not node:
        return head
    elif index == 0:
        node.next = head
        head.prev = node
        head = node
        return head
    else:
        for i in range(index-1):
            if not curr:
                return head
            else:
                curr = curr.next
        tail = curr.next
        if not tail:
            curr.next = node
            node.prev = curr
        else: 
            curr.next = node
            node.prev = curr
            node.next = tail
            tail.prev = node
        return head

def deleteNode(head, index):
    curr = head
    if not head: # no list
        return None
    elif index == 0:
        curr = curr.next
        head.next = None
        if not curr: # only 1 node
            return None
        else:
            curr.prev = None
            head = curr
    else:
        for i in range(index-1):
            if not curr:
                print("Index out of range")
                break
            else:
                curr = curr.next
        if not curr.next:
            print("Index out of range")
        else:
            node = curr.next
            if not node.next:
                node.prev = None
                curr.next = None
            else:
                curr.next = curr.next.next
                curr.next.prev = curr
                node.next = None
                node.prev = None
    return head


#======================= TEST CODE ====================================

def build_list(values):
    """Builds a doubly linked list from a Python list"""
    head = None
    tail = None
    for v in values:
        node = doubleListNode(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head

def to_pylist(head):
    """Converts linked list back to Python list"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def display(head):
    print(" -> ".join(map(str, to_pylist(head))) or "(empty)")


#======================= TEST CASES ====================================
# Insert at head
head = build_list([1, 2, 3])
head = addNode(head, doubleListNode(0), 0)
print("Insert at head:", to_pylist(head))   # [0, 1, 2, 3]

# Insert in middle
head = build_list([1, 2, 3])
head = addNode(head, doubleListNode(9), 2)
print("Insert in middle:", to_pylist(head))  # [1, 2, 9, 3]

# Insert at tail
head = build_list([1, 2, 3])
head = addNode(head, doubleListNode(99), 3)
print("Insert at tail:", to_pylist(head))   # [1, 2, 3, 99]

# Insert in empty list
head = None
head = addNode(head, doubleListNode(5), 0)
print("Insert in empty list:", to_pylist(head))   # [5]

# Delete head
head = build_list([1, 2, 3, 4])
head = deleteNode(head, 0)
print("Delete head:", to_pylist(head))   # [2, 3, 4]

# Delete middle
head = build_list([1, 2, 3, 4])
head = deleteNode(head, 2)
print("Delete middle:", to_pylist(head)) # [1, 2, 4]

# Delete tail
head = build_list([1, 2, 3, 4])
head = deleteNode(head, 3)
print("Delete tail:", to_pylist(head))   # [1, 2, 3]

# Delete single element
head = build_list([42])
head = deleteNode(head, 0)
print("Delete single element:", to_pylist(head)) # []

head = build_list([10, 20, 30, 40])
searchNode(head, 0)   # should print 10
searchNode(head, 2)   # should print 30
searchNode(head, 5)   # should handle out-of-range gracefully

head = build_list([7, 8, 9])
display(head)   # 7 → 8 → 9
display(None)   # (empty)

