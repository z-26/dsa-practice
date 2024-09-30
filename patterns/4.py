"""
Below pattern to print
1
22
333
4444
55555
"""

def print_pattern(n: int):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end="")
        print()



print_pattern(n=5)