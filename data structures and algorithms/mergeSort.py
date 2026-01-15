def merge(left, right):
    i = 0
    j = 0
    new = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    if i >= len(left):
        for k in range(j,len(right)):
            new.append(right[k])
    elif j >= len(right):
        for k in range(j,len(left)):
            new.append(left[k])

    return new


def mergesort(arr):
    if not arr:
        return arr
    
    if len(arr) == 1:
        return arr
    
    l = mergesort(arr[0:len(arr)//2])
    r = mergesort(arr[len(arr)//2:])

    return merge(l,r)

a = [1,6,2,5,8,235,7,23,4,5,67]
print(mergesort(a))