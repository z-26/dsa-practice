def armstrong_number(n: int):
    sum = 0
    num_copy = n
    while n > 0:
        digits = n%10
        sum = sum + digits*digits*digits
        n = n//10
    if sum == num_copy:
        return True
    else:
        return False

print(armstrong_number(n=371))