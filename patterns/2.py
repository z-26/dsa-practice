"""
Below pattern to print
*
**
***
****
"""

def print_pattern(n: int):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

print_pattern(n=5)