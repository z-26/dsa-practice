#print name n times

def print_n_times(n: int, i: int):
    i = i+1
    if i > n:
        return
    print("name")
    print_n_times(n=n, i=i)
    
    
print_n_times(n=5, i=0)

# Time complexity - O(n)
# Space complexity - O(n)

#print_linerly from 1 to n

def print_1_to_n(n: int, i: int):
    if i > n:
        return
    print(i)
    i = i+1
    print_1_to_n(n=n, i=i)

print_1_to_n(n=5, i =1)

#print_ from n to 1

def print_n_to_1(n: int, i: int):
    if i >= n:
        return
    print(n-i)
    i=i+1
    print_n_to_1(n=n, i=i)

print_n_to_1(n=5, i=0)