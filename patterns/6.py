"""
Below pattern to print
12345
1234
123
12
1
"""

def print_pattern(n: int):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end="")
        print()

print_pattern(n=8)