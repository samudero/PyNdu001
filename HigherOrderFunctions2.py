# Higher Order Functions 2: Functional tools [257]

"""
Created on Mon 26 Mar 2018
@author: pandus
"""

# ------------------------ Anonymous function lambda

lambda a: a

lambda a: 2 * a

(lambda a: 2 * a)

(lambda a: 2 * a) (10)      # returns 20
(lambda a: 2 * a) (20)      # returns 40

(lambda x, y: x + y) (10, 20)               # returns 30
(lambda x, y, z: (x + y) * z) (10, 20, 2)   # returns 60

type(lambda x, y: x + y)    # returns "function"

# ------------------------ Lambda usage example 1
# integrate f(x) = x2 from 0 to 2 (numerically)

# without lambda
from scipy.integrate import quad
def f(X):
    return X * X

y, abserr = quad(f, a = 0, b = 2)
print("Int f(x) = x^2 from 0 to 2 = {:f} +- {:g}"
      .format(y, abserr))
# returns --> Int f(x) = x^2 from 0 to 2 = 2.666667 +- 2.96059e-14

# With Lambda
from scipy.integrate import quad
y, abserr = quad(lambda X: X * X, a = 0, b = 0)
print("Int f(x) = x^2 from 0 to 2 = {:f} +- {:g}"
      .format(y, abserr))
# returns --> Int f(x) = x^2 from 0 to 2 = 0.000000 +- 0

# ------------------------ Map
# map(function, sequence)
def f(X): return X ** 2
map(f, [0, 1, 2, 3, 4])
list(map(f, [0, 1, 2, 3, 4]))

list(map(lambda x:x ** 2, [0, 1, 2, 3, 4]))
[X ** 2 for X in [0, 1, 2, 3, 4]]

# ------------------------ Example(maths)
import math
list(map(math.exp, [0, 0.1, 1.]))

# ------------------------ Example(slug)
news = "Python programming occasionally" \
       " more fun than expected"
slug = "-" .join(map(lambda w: w[0:6], news.split()))
slug    # returns: 'Python-progra-occasi-more-fun-than-expect'

# Equivalent list comprehension expression:
slug = "-" .join([w[0:6] for w in news.split()])

# ------------------------ Filter
# filter(function, iterable) --> iterable: returns items

c = "The quick brown fox jumps" .split()
print(c)                # returns --> ['The', 'quick', 'brown', 'fox', 'jumps']

def len_gr_4(s):
    return len(s) > 4

list(map(len_gr_4, c))  # returns --> [False, True, True, False, True]
filter(len_gr_4, c)     # returns --> <filter at 0x7722828>

list(filter(len_gr_4, c))               # returns: ['quick', 'brown', 'jumps']
list(filter(lambda s: len(s) > 4, c))   # returns: ['quick', 'brown', 'jumps']

[s for s in c if len(s) > 4]            # returns: ['quick', 'brown', 'jumps']

# ------------------------ Examples Filter
def is_positive(n):
    return n > 0

list(filter(is_positive,
            [-3, -2, -1, 0, 1, 2, 3, 4]))           # returns: [1, 2, 3, 4]

list(filter(lambda n:n>0,
            [-3, -2, -1, 0, 1, 2, 3, 4]))           # returns: [1, 2, 3, 4]

# List comprehension equivalent:
[x for x in [-3, -2, -1, 0, 1, 2, 3, 4] if x > 0]   # returns: [1, 2, 3, 4]

# ------------------------ Reduce [269]
# functools.reduce(function, iterable, initial) ! value:
# apply function(x, y) from left to right to reduce iterable to a single value.

# Examples:
from functools import reduce
def f(x, y):
    print("Called with x={}" .format(x, y))
    return x + y

reduce(f, [1, 3, 5], 0)
reduce(f, [1, 3, 5], 100)
reduce(f, "test", "")
reduce(f, "test", "FIRST")

# ------------------------ Operator Module [271]
def f(x, y): return x + y
reduce(f, range(10), 0)

# can also be written as:
reduce(operator.add, range(10), 0)

reduce(lambda x, y: x + y, range(10), 0)