def hcf_of_number(n1:int, n2: int):
    for i in range(min(n1,n2), 0, -1):
        if n1%i == 0 and n2%i == 0:
            print(f"The hcf is {i}")
            break
hcf_of_number(n1=20, n2=11)


# eucliean algorithm
# hcf(a,b) = hcf(a%b,b) till one number is zero then other number is hcf
# Time complexity = O(logq min(a,b))

def hcf_using_eucliean(n1:int, n2: int):
    while n1>0 and n2>0:
        if n1>n2:
            n1 = n1%n2
        else:
            n2=n2%n1
    if n1 == 0:
        return n2
    return n1

print(hcf_using_eucliean(n1=52, n2=10))
