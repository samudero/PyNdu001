# Belajar Tuple
"""
Created on Mon Mar 12 2018

@author: pandus
"""

t = (3, 4, 50)  # t for Tuple
t
type(t)

l = [3, 4, 50]
l
type(l)

a = 10, 20, 30
type(a)

t[1]
t[:-1]

x, y, z = 0, 0, 1
b = 54
a, b = b, a

def f(x):
    return x**2, x**3

a, b = f(x)
a, b = f(6) # returns a = 36; b = 216

# ----------------------------------------------------------------
a = 'hello world'   # string example
#a[4] = 'x'  # will give error
a = a[0:3] + 'x' + a[4:]
a           # 'helxo world'

len(a)
min(l)
'w' in a # returns "True" since 'w' is in a
a + ' uhuiy'
3 * a

# -------------------------- Conversion --------------------------
tuple([1, 4, "dog"])    # --> jadi (1, 4, "dog)
list((10, 20, 30))      # --> jadi (10, 20, 30)
list(range(5))

iter([1, 2, 3])