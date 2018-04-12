# Belajar Loops [slide page 65]
"""
Created on Wed Mar 14 2018

@author: pandus
"""
# ------------------------------------------------------------

animals =   ['dog', 'cat', 'mouse']

for animal in animals:
    print("This is the {}".format(animal))

# ------------------------------------------------------------

for i in [0, 1, 2, 3, 4, 5]:
    print("the square of {} is {}".format(i, i**2))

# ------------------------------------------------------------

for i in range(6):
    print("the square of {} is {}".format(i, i**2))

# ------------------------------------------------------------

for i in range(4):
    print("i = {}".format(i))

# ------------------------------------------------------------

for i in [0, 3, 4, 19]:
    print(i)

for animal in ['babi', 'kucing', 'orangutan']:
    print(animal)

for letter in "Hello World":
    print(letter)

for i in range(5):
    print(i)

# ------------------------------------------------------------

a = 42
if a > 0:
    print("a is positive")
else:
    print("a is negative or zero")

# ------------------------------------------------------------

def skip13(a, b):
    result = []
    for k in range(a, b):
        if k == 13:
            pass                # do nothing
        else:
            result.append(k)
    return result

skip13(1, 21)

# ---------------------- WHILE -----------------------------

x = 64
while x > 10:
    x = x // 2
    print(x)

# ------------------------------------------------------------

eps = 1.0

while eps + 1 > 1:
    eps = eps / 2.0
print("epsilon is {}".format(eps))