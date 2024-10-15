def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        # divide
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        # merge
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i +=1
            else:
                arr[k] = right_half[j]
                j +=1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

data = [7,4,8,3,6,1,5,6,9,14,12]
merge_sort(arr=data)
print(data)