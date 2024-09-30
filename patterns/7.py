"""
Below pattern to print
    *    
   ***   
  *****  
 ******* 
*********
"""

# 2i+1

def print_pattern(n: int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()

print_pattern(n=5)