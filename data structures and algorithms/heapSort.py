"""For a node at index i:

Left child = 2*i + 1
Right child = 2*i + 2
Parent = (i - 1) // 2

Last Parent: (n-2)//2
"""

def heapSort(arr,high,low):
    if low >= high:
        return None
    
    heapsize = high-low+1

    for i in range((high-low-2)//2,-1,-1):
        while True:
            left = 2*i + 1
            right = 2*i + 2

            # if no children, stop
            if left >= heapsize:
                break

            # pick the bigger child (if right exists)
            larger = left
            if right <  heapsize and arr[right] > arr[left]:
                larger = right

            # if parent already bigger, stop
            if arr[i] >= arr[larger]:
                break

            # swap and continue sifting
            arr[i], arr[larger] = arr[larger], arr[i]
            i = larger

            print(arr)

    arr[low], arr[high] = arr[high], arr[low]

    heapSort(arr,high-1,low)

a = [1,5,2,5,6,7,12315,16,1,12059,62,3]
heapSort(a,len(a)-1,0)
print(a)