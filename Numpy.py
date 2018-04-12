# Numpy [231]
# is an interface to high performance linear algebra libraries (ATLAS, LAPACK, BLAS)

"""
Created on Fri 23 Mar 2018
@author: pandus
"""

# ------------------------ numpy arrays (vectors)
import numpy as np
a = np.array([1, 4, 10])
type(a)
a.shape
a ** 2
np.sqrt(a)
a > 3

# ------------------------ Array creation
# 1D - array (vector)
from numpy import array
a = array([1, 4, 10])
a
print(a)

# 2D - array (matrix)
B = array([[0, 1.5], [10, 12]])
B
print(B)

# ------------------------ Array Shape
a.shape     # returns (3,) --> len(a.shape) is 1 --> 1D array with 3 elements
B.shape     # returns (2, 2) --> len(B.shape) is 2 --> 2D array with 2x2 elements

# Can use shape attribute to change shape:
B
B.shape             # returns (2,2)
B.shape = (4,)
B                   # returns array([  0. ,   1.5,  10. ,  12. ])

# ------------------------ Array Size
# the total number of elements is given through the size attribute:
a.size
B.size

# the total number of bytes used is given through the nbytes attribute:
a.nbytes
B.nbytes

# ------------------------ Array Type
# for existing array
a.dtype
B.dtype

a2 = array([1, 4, 10], np.float)
a2
a2.dtype

# ------------------------ Important array types
# for numerical calcs, we normally use double floats which are known as 'float64' or short 'float'

a2 = array([1, 4, 10], np.float)
a2.dtype

# ------------------------ Array creation II
np.zeros((3, 3))

np.zeros((4,))          # (4,)--> is tuple

np.zeros(4)             # (4)--> is not tuple

np.ones((2, 7))

# ------------------------ Array Indexing (1D arrays)
x = np.array(range(0, 10, 2))
x                       # array([1, 3, 5, 7, 9])

x[3]

x[4]

x[-1]

# can query length as for any sequence:
len(x)
x.shape         # returns (5,) --> length of 1D array is 5

# ------------------------ Array Indexing (2D arrays)
C = np.arange(12)
C

C.shape = (3, 4)
C

C[0, 0]
C[2, 0]
C[2, -1]
C[-1, -1]

# ------------------------ Array slicing (1D arrays)
# Double colon operator::
# Read as START:END:INDEXSTEP --> if either START or END are omitted, the respective ends are used.
# INDEXSTEP defaults to 1

y = np.arange(10)
y[0:5]
y[0:5:1]

y[0:5:2]
y[:5:2]

y[0:5:1]
y[0:5:-1]

y[5:0:-1]
y[5:0:-2]
y[::-1]

# ------------------------ Creating copies of arrays
copy_y = y[:]
y[::-1]

z = np.zeros(y.shape)

# ------------------------ Array slicing [2D]
C
C[0, :]
C[:, 1]