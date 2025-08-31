class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Value({self.val})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # 1. Display all nodes
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    # 2. Find node at index
    def findAt(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    # 3. Insert node at index
    def insertNode(self, index, val):
        if index < 0 or index > self.size:
            print("Index out of range")
            return

        new_node = ListNode(val)

        # insert at head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.findAt(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self.size += 1

    # 4. Remove node at index
    def removeNode(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index < 0 or index >= self.size:
            print("Index out of range")
            return

        if index == 0:
            to_delete = self.head
            self.head = self.head.next
        else:
            prev = self.findAt(index - 1)
            to_delete = prev.next
            prev.next = to_delete.next

        to_delete.next = None
        self.size -= 1
        return to_delete.val

    # 5. Get current size
    def getSize(self):
        return self.size


# Q1
def move_even_items_to_back(ll: LinkedList):
    curr = ll.head
    if not curr:
        return ll
    else:
        evens = LinkedList()
        count = 0
        evenCount = 0
        while curr:
            if curr.val % 2 == 0:
                evens.insertNode(evenCount, curr.val)
                evenCount += 1
                curr = curr.next
                ll.removeNode(count)
            else:
                curr = curr.next
                count += 1
    newcurr = ll.head
    for i in range(ll.getSize() - 1):
        newcurr = newcurr.next
    newcurr.next = evens.head

    return ll

ll = LinkedList()
for x in [2, 4, 6, 8, 1, 3, 5]:
    ll.insertNode(ll.getSize(), x)
print("Before:"); ll.display()
move_even_items_to_back(ll)
print("After:"); ll.display()
# Expected: odds [1, 3, 5] followed by evens [2, 4, 6]

# Q2
def move_max_to_front(ll: LinkedList):
    count = 0
    maxindex = 0
    max = ll.head.val

    curr = ll.head
    while curr.next:
        if curr.val > max:
            max = curr.val
            maxindex = count
        else:
            pass
        count += 1
        curr = curr.next
    
    ll.removeNode(maxindex)
    ll.insertNode(0, max)
    return ll

ll2 = LinkedList()
for x in [2, 8, 4, 8, 5]:
    ll2.insertNode(ll2.getSize(), x)
print("Before:"); ll2.display()
move_max_to_front(ll2)
print("After:"); ll2.display()
# Expected: [8 -> 2 -> 4 -> 8 -> 5 -> None]
# (the *first* max moves to front)

# Q3
def remove_duplicates_sorted_ll(ll: LinkedList):
    curr = ll.head
    index = 0
    
    while curr.next:
        if curr.val == curr.next.val:
            ll.removeNode(index+1)
        else:
            curr = curr.next
            index += 1
    
    return ll 

ll3 = LinkedList()
for x in [1, 1, 2, 3, 3, 4, 5, 5]:
    ll3.insertNode(ll3.getSize(), x)
print("Before:"); ll3.display()
remove_duplicates_sorted_ll(ll3)
print("After:"); ll3.display()
# Expected: 1 -> 2 -> 3 -> 4 -> 5 -> None
  