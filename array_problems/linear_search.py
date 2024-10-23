def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

print(linear_search(arr=[1,2,5,7,3,2,8,3,7,5,4,4,9,7], num=9))


