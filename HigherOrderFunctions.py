# Higher Order Functions [142]
"""
Created on Mon 19 Mar 2018

@author: pandus
"""


# ------------------------ print_f_table(f)
def print_f_table(f):
    for i in range(6):
        x = i * 0.5
        print("{} {}".format(x, f(x)))


def square(x):
    return x ** 2


print_f_table(square)


# ------------------------ Can we avoid duplication (2)
def print_f_table(f):
    for i in range(6):
        x = i * 0.5
        print("{} {}".format(x, f(x)))


def square(x):
    return x ** 2


def cubic(x):
    return x ** 3

print("Square"); print_f_table(square)
print("Cubic"); print_f_table(cubic)

# ------------------------ Functions are first class objects --> can be given to other functions as arguments
import math
funcs = (math.sin, math.cos)
for f in funcs:
    for x in [0, math.pi/2]:
        print("{} ({:.3f}) = {:.3f}" .format(f.__name__, x, f(x)))
