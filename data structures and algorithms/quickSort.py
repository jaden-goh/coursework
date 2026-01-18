def quicksort(arr, low, high):
    if len(arr) == 1 or len(arr) == 0:
        return None
    
    pivot = high
    curr = low
    for i in range(low, pivot):
        if arr[i] > arr[pivot]:
            pass
        else:
            temp = arr[i]
            arr[i] = arr[curr]
            arr[curr] = temp
            curr += 1

    temp = arr[pivot]
    arr[pivot] = arr[curr]
    arr[curr] = temp

    quicksort(arr, low, curr)
    quicksort(arr, curr, high)

a = [1,5,2,5,6,7,12315,16,1,12059,62,3]

quicksort(a, 0, len(a)-1)
print(a)

# needs work
