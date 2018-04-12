# Default Arguments [155]
"""
Created on Mon 19 Mar 2018
@author: pandus
"""


# ------------------------ Area of rectangles
def area(a, b):
    return a * b


print("The area is {}.".format(area(3, 1)))
print("The area is {}.".format(area(2.5, 1)))
print("The area is {}.".format(area(2.5, 2)))


# ------------------------ Solution 2 [157]
def area(a, b=1):
    return a * b


print("the area is {}".format(area(3)))
print("the area is {}".format(area(2.5)))
print("the area is {}".format(area(2.5, 2)))

# ------------------------ keyword argument values [158]
def f(a: object, b: object, c: object) -> object:
    print("a = {}, b = {}, c = {}"
        .format(a, b, c))

f(1, 2, 3)
f(c=3, a=1, b=2)
f(1, c=3, b=2)
# if we use only keyword arguments in the function call, then we dont need to know the order of the arguments