import math

def print_prime_no(n: int):
    count_divisors = 0
    for i in range(1,int(math.sqrt(n))):
        if n%i == 0:
            count_divisors += 1
            if n/i != i:
                count_divisors += 1
    if count_divisors == 2:
        return True
    else:
        return False


print(print_prime_no(n=11))