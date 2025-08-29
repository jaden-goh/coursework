

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Node: {self}, Value: {self.val}"
    
# Write a function moveOdditemstoback() that moves all odd integers to the back of a linked list.

def moveOdditemstoback(head):
    """
    Reorders the list in-place so that all even-valued nodes come first,
    followed by all odd-valued nodes. Relative order within the even group
    and within the odd group is preserved (stable).

    Time:  O(n)
    Space: O(1) extra (relinks nodes; no new nodes created)
    """
    if head is None or head.next is None:
        return head

    even_head = even_tail = None
    odd_head = odd_tail = None

    curr = head
    while curr.next is not None and isinstance(curr.next.val, int):
        nxt = curr.next           # save next (so we can safely detach curr)
        curr.next = None          # detach curr from the old chain

        if curr.val % 2 == 0:     # even → goes to even chain
            if even_head is None:
                even_head = even_tail = curr
            else:
                even_tail.next = curr
                even_tail = even_tail.next
        else:                     # odd → goes to odd chain
            if odd_head is None:
                odd_head = odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = odd_tail.next

        curr = nxt

    # If there were no evens, all odds remain as-is
    if even_head is None:
        return odd_head
    # Stitch evens to odds (if any)
    even_tail.next = odd_head
    return even_head


# ========================= TEST CASES ===================================
def build_linked_list(input_str):
    tokens = input_str.split()
    head = None
    tail = None

    for token in tokens:
        if not token.isdigit():
            break
        val = int(token)
        new_node = ListNode(val)
        if head is None:
            head = new_node
            tail = head
        else:
            tail.next = new_node
            tail = new_node
    return head

def build_linked_list(input_str):
    tokens = input_str.split()
    head = None
    tail = None
    for token in tokens:
        if not token.isdigit():
            break
        node = ListNode(int(token))
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


# Prints linked list
def print_list(head):
    output = []
    while head:
        output.append(str(head.val))
        head = head.next
    print(" -> ".join(output))


# Test Case
input_str = "1 2 3 4 5 12 923 7 44 87 a"
head = build_linked_list(input_str)

print("Before:")
print_list(head)

head = moveOdditemstoback(head)

print("After:")
print_list(head)