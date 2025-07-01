

"""
Array: fixed size container, elements of same type
 
 Operations:
    Reading O(1): random access memory can access any index instantly
    Traversal O(n): read all values
    Writing O(1): 
        for STATIC ARRAYS: fixed space is such that you are not able to contain new elements once filled, creates a new static array
        for DYNAMIC ARRAYS: 
    Insertion O(n): imagine inserting in between 2 numbers, all numbers on the right have to be shifted to the next position (assuming enough space)
    Deletion O(n): as elements need to be shifted left  
                    
"""

myArray = []