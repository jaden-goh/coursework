""" Q1 Given an array of n elements. Find two elements in the array such that their sum is
equal to K. The two elements can be the same element. Once a pair of elements is
found, the program can be terminated. The function prototype is given below:"""

def dualSearch(A, size, K):
    ans = []
    for i in range(0,size):
        for j in range(0,size):
            if A[i] + A[j] == K:
                ans.append(i), ans.append(j)
                break
            else:
                pass
    return ans

"""
Q2 Given a sorted array of n elements (you can use merge sort to sort the array).
Find two elements in the array such that their sum is equal to K. The two
elements can be the same element. Once a pair of elements are found, the
program can be terminated. The results may be different from the results of
Question 1. 
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0  # Pointer for the left array
    j = 0  # Pointer for the right array

    # Compare elements from left and right and add the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left array
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def dualSortedSearch(A,size,K):
    ans = []
    A = merge_sort(A)
    
    i = 0
    j = size -1

    while i<=j:
        if A[i] + A[j] > K:
            j -= 1
        elif A[i] + A[j] < K:
            i += 1
        else:
            ans.append(i), ans.append(j)
            return ans
    return False

"""
Q4 Given two arrays num1 and num2. Both are sorted in an ascending order.
The length is m and n, respectively. Please find the median of the two
arrays with time complexity being 𝑂(log(𝑚+𝑛)). You can apply binary
search to partition the arrays. 
"""
def findMedian(num1, num2):
    if len(num2) < len(num1):
        num1, num2 = num2, num1
    # num 1 will always be shorter
    
    total = len(num1) + len(num2)
    half = total //2

    # partitioning
    l,  r = 0, len(num1) - 1
    
    while True:
        mid1 = (l+r)//2 # index of midpoint
        mid2 = half - mid1 - 2 # index of midpoint, not size 

        left1 = num1[mid1] if mid1 >= 0 else float("-infinity")
        right1 = num1[mid1+1] if mid1+1 < len(num1) else float("infinity") 

        left2 = num2[mid2] if mid2 >= 0 else float("-infinity")
        right2 = num2[mid2+1] if mid2+1 < len(num2) else float("infinity") 

        if left1 < right2 and right1 < left2:
            # odd
            if total % 2 == 1:
                return min(right1, right2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            r = mid1 - 1
        else:
            l = mid1 + 1