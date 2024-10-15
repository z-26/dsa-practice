def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break

data = [3,2,5,3,7,1]
bubble_sort(arr=data)
print(data)