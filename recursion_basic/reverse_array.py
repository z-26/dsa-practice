def swap(arr:list, l:int, r: int):
    arr[l], arr[r] = arr[r], arr[l]
    return arr

def reverse_array(arr:list, l:int):
    r = len(arr)-1-l
    if l >= r:
        return
    swap(arr=arr, l=l, r=r)
    reverse_array(arr=arr, l=l+1)
    return arr

print(reverse_array(arr=[1,2,3,4,5], l=0))