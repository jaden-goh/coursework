

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Node: {self}, Value: {self.val}"
    
def duplicateReverse(head):
    rhead = None
    curr = head
    if head is None:
        return None
    else:
        while curr is not None:
            new = ListNode(curr.val)
            new.next = rhead
            rhead = new
            curr = curr.next
    return rhead

# ========================TEST CASES=================================

def build_linked_list(values):
    """Builds a linked list from a Python list and returns the head."""
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
    """Converts a linked list back into a Python list of values."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

head = build_linked_list([1, 2, 3, 4, 5])
print(list_to_pylist(duplicateReverse(head))) 
