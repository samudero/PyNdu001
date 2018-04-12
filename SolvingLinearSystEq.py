# Solving Linear Systems of Equations [249]
# using Numpy

"""
Created on Sun 25 Mar 2018
@author: pandus
"""

# ------------------------ linear algebra
import numpy as numpy
A = numpy.array([[1, 0], [0, 2]])
b = numpy.array([1, 4])

from numpy import linalg as LA

x = LA.solve(A, b)
x

numpy.dot(A, x)         # Computing A * x
                        # returns array([ 1.,  4.]) --> this should be b

# ------------------------ Plotting arrays (vectors)
import pylab
import numpy as N

t = N.arange(0, 10 * N.pi, 0.01)
y = N.cos(t)

pylab.plot(t, y)
pylab.xlabel('t')
pylab.ylabel('y(t)')
pylab.show()