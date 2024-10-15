def selection_sort(arr):
    for i in range (len(arr)-1):
        min_indddex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_indddex]:
                min_indddex = j
        arr[i], arr[min_indddex] = arr[min_indddex], arr[i]

data = [9,7,6,14,5]
selection_sort(arr=data)
print(data)