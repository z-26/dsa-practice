"""
Below pattern to print
****
****
****
****
"""


def print_pattern():
    for i in range(4):
        for j in range(4):
            print("*", end="")
        print()


print_pattern()