def quicksort(arr, low, high):
    # Base case: if the current subarray has 0 or 1 elements, it's already sorted
    if low >= high:
        return

    # Choose pivot as the last element in the current subarray
    pivot = high
    print(f"\nQUICKSORT on indices [{low}, {high}] -> {arr[low:high+1]}")
    print(f"Pivot chosen: index {pivot}, value {arr[pivot]}")

    # curr tracks where the next <= pivot element should go
    curr = low

    # Partition step: move all elements <= pivot to the left side
    for i in range(low, pivot):
        print(f"Compare arr[{i}] = {arr[i]} with pivot = {arr[pivot]}")
        if arr[i] > arr[pivot]:
            # Element stays on the right side of the partition
            print("  No swap (greater than pivot)")
        else:
            # Swap arr[i] with arr[curr] to grow the <= pivot region
            print(f"  SWAP partition: index {i} <-> index {curr} | {arr[i]} <-> {arr[curr]}")
            temp = arr[i]
            arr[i] = arr[curr]
            arr[curr] = temp
            print("   array now:", arr)

            curr += 1  # Expand the <= pivot region

    # Finally, move pivot into its correct sorted position (at index curr)
    print(f"SWAP pivot into place: index {pivot} <-> index {curr} | {arr[pivot]} <-> {arr[curr]}")
    temp = arr[pivot]
    arr[pivot] = arr[curr]
    arr[curr] = temp
    print("   array now:", arr)
    print(f"Pivot {arr[curr]} placed at final index {curr}")

    # Recursively sort left and right subarrays (excluding the pivot)
    print(f"Recurse LEFT  on indices [{low}, {curr-1}]")
    print(f"Recurse RIGHT on indices [{curr+1}, {high}]")

    quicksort(arr, low, curr - 1)   # Left side of pivot
    quicksort(arr, curr + 1, high)  # Right side of pivot


a = [1,5,2,5,6,7,12315,16,1,12059,62,3]
quicksort(a, 0, len(a)-1)

print("\nFINAL SORTED ARRAY:", a)
