# List comprehension [178]
# follow the mathematical "set builder notation"
# convenient way to process a list into another list (without for-loop)

"""
Created on Wed 21 Mar 2018
@author: pandus
"""

# ------------------------ Examples
[2 ** i for i in range(10)]

[x ** 2 for x in range(10)]

[x for x in range(10) if x >5]

# ------------------------ Example 1:
xs = [i for i in range(10)]     # output xs= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ys = [x ** 2 for x in xs]

# ------------------------ Example 2:
import math
xs = [0.1 * i for i in range(5)]

ys = [math.exp(x) for x in xs]

# ------------------------ Example 3:
words = 'The quick brown fox jumps \
over the lazy dog' .split()

print (words)

# +++_+_+_+_+_++_+_+_+_+__++_+
stuff = [[w.upper(), w.lower(), len(w)]
         for w in words]

for i in stuff:
    print(i)

# ------------------------ extend with if CONDITION
[i for i in range(10)]

[i for i in range(10) if i > 5]

[i for i in range(10) if i ** 2 > 5]