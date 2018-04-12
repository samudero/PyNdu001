# Root Finding [202]

"""
Created on Fri 23 Mar 2018
@author: pandus
"""

# ------------------------ Using bisection algorithm from scipy
from scipy.optimize import bisect

def f(x):
    """returns f(x) = x^3 - 2x^2. Has roots at x = 0 (double root) and x = 2"""
    return x ** 3 - 2 * x ** 2

# Main program starts here
x = bisect(f, a = 1.5, b = 3, xtol = 1e-6)

print("Root x is approx. x = {:14.12g}." .format(x))
print("The error is less than 1e-6.")
print("The exact error is {}." .format(2 - x))

# ------------------------ The Newton method
from scipy.optimize import newton

def f(x):
    """returns f(x) = x^3 - 2x^2. Has roots at x = 0 (double root) and x = 2"""
    return x ** 3 - 2 * x ** 2

# main program starts here
x = newton(f, x0 = 1.6)

print("Root x is approx. x = {:14.12g}." .format(x))
print("The error is less than 1e-6.")
print("The exact error is {}." .format(2 - x))

# ------------------------ Using BrentQ algorithm from scipy
from scipy.optimize import brentq

def f(x):
    """returns f(x) = x^3 - 2x^2. Has roots at x = 0 (double root) and x = 2"""
    return x ** 3 - 2 * x ** 2

# main program starts here
x = brentq(f, a = 1.5, b = 3, xtol = 1e-6)

print("Root x is approx. x = {:14.12g}." .format(x))
print("The error is less than 1e-6.")
print("The exact error is {}." .format(2 - x))

# ------------------------ Using fsolve algorithm from scipy
from scipy.optimize import fsolve       # multidimensional solver

def f(x):
    """returns f(x) = x^3 - 2x^2. Has roots at x = 0 (double root) and x = 2"""
    return x ** 3 - 2 * x ** 2

# main program starts here
x = fsolve(f, x0 = [1.6])

print("Root x is approx. x = {}." .format(x))
print("The error is less than 1e-6.")
print("The exact error is {}." .format(2 - x[0]))

