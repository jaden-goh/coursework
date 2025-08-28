#* 
# Stacks: Implement with L-L in this course
# Operations: Push (to top of stack), Pop (remove top of stack), Peek/Top (check value/look at top of stack), is_empty, get size #
# LIFO Structure, the idea with using linked list is that head (the first node in the list) is the top of the stack
# 

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Value: {self.val}"
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

def push(head: Stack, val: int):
    new = ListNode(val)
    new.next = head.top
    head.top = new
    head.size += 1
    return head

def pop(head: Stack):
    if is_empty(head):
        raise IndexError("Stack is Empty!")
    else:
        curr = head.top
        head.top = curr.next
        curr = None
    head.size -= 1
    return head

def is_empty(head):
    if not head.top:
        return True
    else:
        return False

def peek(head):
    if is_empty(head):
        raise IndexError("Stack is Empty!")
    else:
        return head.top.val


    
colour1 = ListNode("Blue")
colour2 = ListNode("Red")  
colour3 = ListNode("Green")

num1 = ListNode(1)
num2= ListNode(2)
num3= ListNode(3)
num4= ListNode(4)

num1.next = num2
num2.next = num3
num3.next = num4
    

