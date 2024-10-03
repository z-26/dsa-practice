def palindrome_number(n: int):
    num_copy = n
    new_num = 0
    while n > 0:
        digits = n%10
        n = n//10
        new_num = new_num*10 + digits
    if new_num == num_copy:
        return True
    else:
        return False

print(palindrome_number(n=1331))