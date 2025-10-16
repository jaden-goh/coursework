def binarySearch(arr, a):
    l = 0
    r = len(arr) - 1

    while l != r:
        mid = (l+r)//2
        temp = arr[mid]
        if temp > a:
            r = mid
        elif temp < a:
            l = mid 
        else:
            return f"Found: Number {a} at Index {mid}"
            
    return "Number not found!"

a = [1,2,3,4,5]
print(binarySearch(a, 3))