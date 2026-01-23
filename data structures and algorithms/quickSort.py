def quicksort(arr, low, high):
    if low >= high:
        return None #base case, if indexes are narrow enough, go back out of loop
    
    pivot = high
    curr = low # denotes the swapping index
    for i in range(low, pivot): # from starting index, if value is <= the pivot value, swap with curr, move curr index up
        if arr[i] < arr[pivot]:
            pass 
        else:
            temp = arr[i]
            arr[i] = arr[curr]
            arr[curr] = temp
            curr += 1

    temp = arr[pivot]
    arr[pivot] = arr[curr]
    arr[curr] = temp

    quicksort(arr, low, curr-1)
    quicksort(arr, curr+1, high)

a = [1,5,2,5,6,7,12315,16,1,12059,62,3]

quicksort(a, 0, len(a)-1)
print(a)

# needs work
