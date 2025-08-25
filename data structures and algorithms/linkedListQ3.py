
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Node: {self}, Value: {self.val}"
    
#Write a function split()that copies the contents of a linked list into two other linked lists

def split(head):
    curr = head
    evenHead = None
    oddHead = None

    count = 0

    while curr is not None:
        if count%2 == 0:    
            if evenHead is None:
                evenHead = curr
                even = evenHead
                curr = curr.next
            else:
                even.next = curr
                even = even.next
                curr = curr.next
                even.next = None

        elif count%2 == 1:
            if oddHead is None:
                oddHead = curr
                odd = oddHead
                curr = curr.next
            else:
                odd.next = curr
                odd = odd.next
                curr = curr.next
                odd.next = None

        count += 1
    
    return evenHead, oddHead

# =========================== TEST CASES ========================================

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

def print_list(head):
    """Pretty prints a linked list."""
    print(" -> ".join(map(str, list_to_pylist(head))) or "(empty)")

                
# Build a list
head = build_linked_list([1, "a", 1 ,5,7,78 ,1])

# Call your function
evenHead, oddHead = split(head)  # depending on how you want to return things

# Print results
print("Even list:")
print_list(evenHead)
print("Odd list:")
print_list(oddHead)

