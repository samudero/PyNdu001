# Printing [page 119]
"""
Created on Tue Mar 15 2018

@author: pandus
"""

# ------------------------ general
print("dog", "cat", 42)
print("Dog", end='');
print("Cat")

# ------------------------ common strategy for print command
s = "I am the string to be printed"
print(s)

# ------------------------ % operator syntax
import math

p = math.pi
"%f" % p  # format p as float (%f) --> returns string
"%d" % p  # format p as integer (%d)
"%e" % p  # format p in exponential style
"%g" % p  # format using fewer characters

'the value of pi is approx %f' % p
'%d is my preferred number' % 42

# combining multiple objects
"%d times %d is %d" % (10, 42, 10 * 42)

"pi=%f and 3*pi=%f is approx 10" % (p, 3 * p)

# ------------------------ % fixing width and/ or precision of resulting string [125]
'%f' % 3.14  # default width and precision
'%10f' % 3.14  # 10 characters long
'%10.2f' % 3.14  # 10 long, 2 post-dec digits
'% .2f' % 3.14  # 2-post decimal digits
'% .14f' % 3.14  # 14 post-decimal digits

# string
"% 10s" % "Apple"
"% 10s" % "Banana"

# ------------------------ % Common formatting specifiers [127]
# Astronomical Unit {AU}
AU = 149597870700  # AU [m]
"% f" % AU  # line 1 in table

# ------------------------ % Summary %-operator for printing [128]
import math

print("My pi = % .2f." % math.pi)

# Print multiple values:
print("a=%d b=%d" % (10, 20))

# New style string formatting
"{} needs {} pints".format('Pandu', 4)
"{0} needs {1} pints".format('Pjanic', 4)
"{name} needs {number} pints".format(name='pedro', number=4)
"Pi is approx {:f}.".format(math.pi)

"Pi is approx {:6.2f}".format(math.pi)
"Pi is approx {:.2f}.".format(math.pi)

# ------------------------ method __str__ --> is called when apply str function to object 'a'
a = 3.14
a.__str__()
str(a)

b = [3, 4.2, ['apple', 'banana'], (0, 1)]
str(b)

# ------------------------ the method x.__str__ is called implicitly, when we
# (1)
b = [3, 4.2, ['apple', 'banana'], (0, 1)]
b.__str__()

# (2)
str(b)

# (3)
"% s" % b

# (4)
"{}".format(b)

# (5)
print(b)

# ------------------------ 'repr' function --> convert a given object into an as accurate as possible string representation
import datetime

t = datetime.datetime.now()  # current date and time
str(t)  # inofficial representation
repr(t)

# ------------------------ 'eval' function --> accepts a string, and evaluates string
x = 1
eval('x + 1')

s = "[10, 20, 30]"
type(s)  # --> returns 'string'
eval(s)  # --> returns [10, 20, 30]
type(eval(s))  # --> returns 'list'

# ------------------------ 'eval' and 'repr' function
i = 42
type(i)  # --> returns 'int'
repr(i)
type(repr(i))  # --> returns 'str'
eval(repr(i))
type(eval(repr(i)))  # --> returns 'int'

# ------------------------ the datetime example:
import datetime

t = datetime.datetime.now()
t_as_string = repr(t)
t_as_string

t2 = eval(t_as_string)
t2

type (t2)           # --> returns 'datetime.datetime'
t == t2             # --> returns "true"