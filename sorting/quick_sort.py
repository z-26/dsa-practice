def quick_sort(arr, low, high):
    if low<high:
        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index-1)
        quick_sort(arr, partition_index+1, high)


def partition(arr, low, high):
    pivot = arr[low]

    i = low+1
    j = high

    while True:
        # Move i to the right until an element greater than or equal to the pivot is found
        while i <= j and arr[i]< pivot:
            i += 1
        
        # Move j to the left until an element less than or equal to the pivot is found
        while j >= i and arr[j] > pivot:
            j -= 1
        
        # If the pointers cross, break the loop
        if i >= j:
            break

         # Swap the elements at i and j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    # Place the pivot in its correct position by swapping it with arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    # Return the partition index
    return j

data = [2,4,1,5,2,3,9,4,7,15,12]
quick_sort(arr=data, low=0, high=len(data)-1)
print(data)