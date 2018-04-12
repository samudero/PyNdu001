# Namespaces [163]
# Global variables --> defined in main program
# local variables --> defined e.g. in functions
# built-in functions
"""
Created on Tue 20 Mar 2018
@author: pandus
"""

# ------------------------ global - local
def f():
    x = 'I am local'
    print(x)

x = 'I am global'

f()             # produces "I am local"
print(x)        # produces "I am global"

# ------------------------ We can read global variables from functions
def f():
    print(x)

x = 'I am global'
f()

# ------------------------ But local variables "shadow" global variables:
def f():
    y = "I am local y"      # this variable is being "shadowed"
    print(x)
    print(y)

x = 'I am global x'
y = 'I am global y'
f()

print("back in main:")
print(y)