
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Node: {self}, Value: {self.val}"
    
#* Write the function removeNode()using the LinkedListstructure defined in the lecture materials. The function should remove a node at the specified index from the linked list. 

def removeNode(head, index):
    curr = head
    
    if index == 0:
        return head.next
    
    else:
        i = 0
        while i < index-1:
            if curr.next == None:
                print("This index cannot be deleted!")
            else:
                curr = curr.next
            i += 1
        
        print(curr.val)

        curr.next = curr.next.next
        return head

# ======================= TEST CASE =================================
def build_linked_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def list_to_pylist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = build_linked_list(list(range(1, 11)))  # [1..10]
head = removeNode(head, 5)
print(list_to_pylist(head))   # Expected: remove element at index 5


























