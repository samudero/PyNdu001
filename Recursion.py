# Recursion [194]

"""
Created on Thu 23 Mar 2018
@author: pandus
"""

# ------------------------ Example: Factorial
# computing factorial can be done by computing (n-1)!n, --> reduce the problem of size n to a problem of size n-1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(0)            # returns 0
factorial(2)
factorial(4)            # returns 24

# ------------------------ recursion example Fibonacci numbers
def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n - 2) + f(n - 1)
