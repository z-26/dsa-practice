def largest_element(arr):
    largest_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[largest_index]:
            largest_index = i
    return arr[largest_index]

print(largest_element(arr=[1,4,2,8,2,4,5,9,5,10,5,3,7]))