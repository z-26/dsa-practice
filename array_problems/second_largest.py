def second_largest(arr):
    largest = arr[0]
    second_largest = -1
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        if i > second_largest and i < largest:
            second_largest = i
    return largest, second_largest

print(second_largest(arr=[1,6,3,7,3,2,6,9,3,9,8]))
            
