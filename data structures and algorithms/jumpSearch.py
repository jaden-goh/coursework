def jumpSearch(arr, a):
    step = min(1, int(len(arr) ** 0.5))
    i = 0

    while i < len(arr) - 1:
        if a == arr[i]:
            return f"Number {a} found at Index {i}"
        elif a < arr[i]:
            break
        else:
            i += step
    
    for j in range(i-step+1, i+1):
        if arr[j] == a:
            return f"Number {a} found at Index {j}"
        else:
            pass

    return "Not Found"

a = [1,2,3,4,5]
print(jumpSearch(a, 5))


