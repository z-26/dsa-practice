"""
Below pattern to print
1
12
123
1234
"""

def print_pattern(n: int):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print()

print_pattern(n=5)