# some things revisited [page 80]
"""
Created on Wed Mar 14 2018

@author: pandus
"""
# ------------------------------------------------------------
a = [0, 2, 4, 6]    # Bind name 'a' to list

b = a
b[1] = 10

id(a) == id(b)      # output: "True"

# -------------------------- EXAMPLE 1 --------------------
a = 1
b = 1.0
id(a); id(b)    # gives different number, not in the same place in memory
a is b      # output: "False" --> not the same objects
a == b      # output: "True"  --> but carry the same value

# -------------------------- EXAMPLE 2 --------------------
a = [1, 2, 3]
b = a       # b is reference to object of a
a is b      # output: "True" --> thus they are the same
a == b      # output: "True" --> the value is the same

# -------------------------- FUNCTIONS - SIDE EFFECT --------------------
def sum(xs):
    s = 0
    for i in range(len(xs)):
        s = s + xs.pop()
    return s

xs = [10, 20, 30]
print("xs = {}; ".format(xs), end='')
print("sum(xs) = {}; ".format(sum(xs)), end='')
print("xs = {}".format(xs))

# ---------------- Use indices to iterate over list
def sum(xs):
    s = 0
    for i in range(len(xs)):
        s = s + xs[i]
    return s

# ---------------- iterate over list elements directly
def sum(xs):
    s = 0
    for elem in xs
        s = s + elem
    return s
