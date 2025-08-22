class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return f"Node: {self}, Value: {self.val}"
    
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
                print(None)
                break
            else:
                curr = curr.next
        print(curr.val)

def addNode(head,node,index):
    curr = head
    if not head:
        return None
    elif not node:
        return None
    else:
        for i in range(index-1):
            if not curr:
                print(None)
                break
            else:
                curr = curr.next
        tail = curr.next
        curr.next = node
        node.next = tail
    

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

num2.next = num2.next.next # num2.next (3) becomes num2.next.next (4), 3 has no pointers, removed by garbage collector

cur = num1
while cur.next:
    print(cur.val)
    cur = cur.next
print(cur.val) # Prints 1 2 4 (3 deleted)
 
displayNodes(num1)

searchNode(num1, 1)

addNode(num1, colour1, 2)
displayNodes(num1)