"""For a node at index i:

Left child = 2*i + 1
Right child = 2*i + 2
Parent = (i - 1) // 2

Last Parent: (n-2)//2
"""

def heapSort(arr):

    heapsize = len(arr)
    while heapsize > 0:
        for i in range((heapsize-2)//2,-1,-1):
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

        arr[0], arr[heapsize-1] = arr[heapsize-1], arr[0]
        heapsize -= 1
        

a = [1,5,2,5,6,7,12315,16,1,12059,62,3]
heapSort(a)
print(a)