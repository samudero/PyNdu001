# Module files [150]
# bundle functions that are used repeatedly and belong to the same subject area into one module file
# also called "library"
"""
Created on Mon 19 Mar 2018
@author: pandus
"""

# ------------------------ module2.py
def useful_function():
    pass

def test_for_useful_function():
    print("Running self test...")

if __name__ == "__main__":
    test_for_useful_function()
else:
    print("Setting up library")
    # initialisation code that might be needed if imported as a library
