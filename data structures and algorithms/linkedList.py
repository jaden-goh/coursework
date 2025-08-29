"""
2. Linked Lists

Properties:
Nodes with values + pointers. Variants: Singly, Doubly, Circular.

Functions:

Access by index: O(n)

Search: O(n)

Insert/Delete at head: O(1)

Insert/Delete at tail: O(1) (if tail pointer known; otherwise O(n))

Space: O(n) (extra pointers)
"""



class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Value: {self.val}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
def displayNodes(list):
    curr = list.head
    while curr:
        print(curr.val)
        curr = curr.next
    print(None)

def searchNode(list, index):
    if not list.head:
        print(None)
    else:
        curr = list.head
        for i in range(index):
            if not curr:
                print(None)
                break
            else:
                curr = curr.next
        print(curr.val)

def addNode(list,node,index):
    curr = list.head
    if not list.head:
        list.head = node
        return list
    elif not node:
        return list
    elif index == 0:
        node.next = list.head
        list.head = node
        return list
    else:
        for i in range(index-1):
            if not curr:
                return list
            else:
                curr = curr.next
        tail = curr.next
        curr.next = node
        node.next = tail
        return list

def deleteNode(list, index):
    curr = list.head
    if not list.head:
        return None
    elif index == 0:
        curr = curr.next
        list.head.next = None
        list.head = curr
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
            curr.next = curr.next.next
    return list
    


