def findMinMax(arr, start, end):
    ans = []

    if end-start == 0:
        ans[0] = arr[0]
        ans[1] = arr[0]
        return ans
    
    if end-start == 1:
        ans[0] = arr[0] if arr[0] < arr[1] else arr[1]
        ans[1] = arr[0] if arr[0] > arr[1] else arr[1]
        return ans
    
    mid = (start + end)// 2
    minMaxL = findMinMax(arr, start, mid)
    minMaxR = findMinMax(arr, mid, end)

    
    ans[0] = minMaxL[0] if minMaxL[0] < minMaxR[0] else minMaxR[0]
    ans[1] = minMaxL[1] if minMaxL[1] > minMaxR[1] else minMaxR[1]

    return ans

a = [1,3,5,5,2,4,129,6,12,6]
b = findMinMax(a, 0, len(a))

print(b)

    