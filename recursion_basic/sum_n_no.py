#parameter method
def sum_of_numbers(i:int, sum:int):
    if i<1:
        print(sum)
        return
    sum_of_numbers(i=i-1,sum=sum+i)

sum_of_numbers(i=3, sum=0)

# function_method
def sum_n(n:int):
    if n==0:
        return 0
    return n + sum_n(n-1)

print(sum_n(n=4))