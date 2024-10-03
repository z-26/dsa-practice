# Method involves strings

def reverse_number(n: int):
    new_num = ""
    while n > 0:
        digits = n%10
        n = n//10
        new_num = new_num+str(digits)
    return int(new_num)

print(reverse_number(n=34500))


# method involving just the digits concept

def reverse_number2(n: int):
    new_num = 0
    while n > 0:
        digits = n%10
        n = n//10
        new_num = new_num*10 + digits
    return new_num

print(reverse_number2(n=34500))