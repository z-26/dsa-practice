"""
Below pattern to print
*    
**   
***  
**** 
*****
**** 
***  
**   
*    
"""

def print_pattern(n: int):
    for i in range(2*n-1):
        stars = i+1
        if i >= n:
            stars = 2*n-i-1
        for j in range(stars):
            print("*", end="")
        print()


print_pattern(n=5)