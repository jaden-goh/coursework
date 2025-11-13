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

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")

def dualSortedSearch(A,size,K):
    ans = []
    A = merge_sort(A)
    
    for i in range(0,size):
        l = 0
        r = size-1
        mid = (l+r) // 2
        while mid < size-1:
            if A[i] + A[mid] < K:
                mid = (mid + size - 1) // 2
            elif A[i] + A[mid] = 