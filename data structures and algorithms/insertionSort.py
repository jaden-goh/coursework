

def InsertionSort(arr):
    for i in range(1 , len(arr)):
        j = i-1
        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    return arr

# Test

a = [1,3,5,5,2,4,1,6,12,6]
b = InsertionSort(a)

print(b)