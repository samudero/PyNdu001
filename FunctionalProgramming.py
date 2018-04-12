# Functional Programming

"""
Created on Wed 28 Mar 2018
@author: pandus
"""

# ------------------------ Standard example
res = []
for x in range(5):
    res.append(x ** 2)

res

# ------------------------
[x ** 2 for x  in range(5)]

list(map(lambda x: x ** 2, range(5)))

# ------------------------ Returning function objects
# We've seen that we can pass function objects as arguments to a function
# now we can look at functions that returns function objects

def make_add42():
    def add42(x):
        return x + 42
    return add42

add42 = make_add42()
print(add42(2))                         # Output is "44"

# ------------------------ Closures
# is a function with bound variables

import math

def make_adder(y):
    def adder(x):
        return x + y
    return adder

add42 = make_adder(42)
addpi = make_adder(math.pi)

print(add42(2))                         # Output is 44
print(addpi(-3))                        # Output is 0.14159265358979312