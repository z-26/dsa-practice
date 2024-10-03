import math

# bigO(n)
def print_divisors(n: int):
    divisors = []
    for i in range(1,n+1):
        if n%i == 0:
            print(i, end=" ")
            divisors.append(i)
    print()
    return divisors

print(print_divisors(n=36))


# more optimised code
# bigO(nlogn)
def print_divisors2(n: int):
    divisors = []
    for i in range(1,int(math.sqrt(n))):
        if n%i == 0:
            divisors.append(i)
            if n/i != i:
                divisors.append(int(n/i))
    divisors.sort()
    return divisors

print(print_divisors2(n=36))