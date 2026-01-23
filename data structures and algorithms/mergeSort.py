# Time: O(n log n)
# Space: O(n) for the merged arrays + O(log n) recursion stack  -> overall O(n)

def merge(left, right):
    # i walks through left, j walks through right
    i = 0
    j = 0
    new = []  # this will store the merged, sorted result

    print(f"\nMERGE called with:")
    print("  left :", left)
    print("  right:", right)

    # As long as BOTH lists still have elements, take the smaller front element
    while i < len(left) and j < len(right):
        print(f"  Compare left[{i}]={left[i]} vs right[{j}]={right[j]}")

        if left[i] <= right[j]:
            # Take from left (stable: ties go left first)
            new.append(left[i])
            print(f"   -> append left[{i}]={left[i]} | new = {new}")
            i += 1
        else:
            # Take from right
            new.append(right[j])
            print(f"   -> append right[{j}]={right[j]} | new = {new}")
            j += 1

    # One side is now exhausted; append the leftover elements from the other side
    if i >= len(left):
        print(f"  Left exhausted, append remaining right from index {j}: {right[j:]}")
        for k in range(j, len(right)):
            new.append(right[k])
            print(f"   -> append right[{k}]={right[k]} | new = {new}")

    elif j >= len(right):
        print(f"  Right exhausted, append remaining left from index {i}: {left[i:]}")
        # NOTE: leftover from LEFT starts at i (not j)
        for k in range(i, len(left)):
            new.append(left[k])
            print(f"   -> append left[{k}]={left[k]} | new = {new}")

    print("MERGE result:", new)
    return new


def mergesort(arr):
    print(f"\nMERGESORT called on: {arr}")

    # Base case 1: empty list is already sorted
    if not arr:
        return arr

    # Base case 2: single element list is already sorted
    if len(arr) == 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left_half = arr[0:mid]
    right_half = arr[mid:]

    print(f"  Split into left={left_half}, right={right_half}")

    # Recursively sort each half
    l = mergesort(left_half)
    r = mergesort(right_half)

    # Merge the two sorted halves
    result = merge(l, r)
    print(f"  mergesort returning: {result}")
    return result


a = [1, 6, 2, 5, 8, 235, 7, 23, 4, 5, 67]
print("\nFINAL SORTED ARRAY:", mergesort(a))
