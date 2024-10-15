def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

data = [6,4,8,9,2,1,4,7]
insertion_sort(arr=data)
print(data)