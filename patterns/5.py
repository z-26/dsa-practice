"""
Below pattern to print
*****
****
***
**
*
"""

def print_pattern(n: int):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()

print_pattern(n=8)

