def count_digits(n:int):
    count = 0
    while n > 0:
        count += 1
        n = n//10
    return count

print(count_digits(n=1897491604))