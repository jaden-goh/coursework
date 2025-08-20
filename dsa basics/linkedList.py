class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        print(f"Node: {self}, Value: {self.val}")

colour1 = ListNode("Blue")
colour2 = ListNode("Red")  
colour3 = ListNode("Green")

colour1.next = colour2
colour2.next = colour3

print(colour1.next.next.val)


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
 