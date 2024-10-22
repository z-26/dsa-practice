def isSorted(n,  a) -> int:
    # Write your code here.
    for i in range(1, n):
        if a[i] >= a[i-1]:
            pass
        else:
            return False
    return True

print(isSorted(n=5,a=[1,2,3,4,5]))