# Exceptions [page 102]
"""
Created on Tue Mar 15 2018

@author: pandus
"""

# ------------------------ Exception example
import sys
try:
    f = open('myfilename.dat', 'r')
except FileNotFoundError:
    print("The file couldn't be found." + "This program stops here.")
    sys.exit(1)                         # a way to exit the program

for line in f:
    print(line, end='')
f.close()

# ------------------------ Alternative Solution
import sys
try:
    f = open('myfilename.txt', 'r')
except OSError as error:
    print("The file couldn't be opened." + "This program stops here.")
    print("Details: {}".format(error))
    sys.exit(1)                         # a way to exit the program

for line in f:
    print(line, end='')
f.close()