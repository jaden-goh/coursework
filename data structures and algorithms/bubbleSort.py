def check(arr):
    for i in range(0, len(arr)-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            return False
    return True

def bubbleSort(arr):
    while not check(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
            else:
                pass
    return arr    

a = [1, 2, 5, 4, 12, 124, 24, 59, 33]
print(bubbleSort(a))