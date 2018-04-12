# Reading and Writing files [page 88]
"""
Created on Wed Mar 14 2018

@author: pandus
"""
# ------------------------ Writing a text file
f = open('test.txt', 'w')       # write
f.write("first line\nsecond line")
f.close()

# ------------------------ Reading a text file
f = open('test.txt', 'r')       # read
lines = f.readlines()
f.close()

lines           # returns: ['first line\n', 'second line']

# ------------------------ Context manager
with open('test.txt', 'r') as f:
    data = f.read()

data