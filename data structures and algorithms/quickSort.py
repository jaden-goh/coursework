def quicksort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return None
    
    pivot = len(arr)-1
    curr = 0
    for i in range(0:pivot):
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

    quicksort(arr[0:curr+1])
    quicksort(arr[curr+1::])

a = [1,5,2,5,6,7,12315,16,1,12059,62,3]
quicksort(a)
print(a)