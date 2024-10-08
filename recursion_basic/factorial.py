def factorial(n:int):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(n=7))


# using a for loop
def factorial_normal(n:int):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print(factorial_normal(n=4))