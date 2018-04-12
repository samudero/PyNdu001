# Original FIFO Solution

"""
Created on Wed 04 Apr 2018
@author: pandus
"""

# ------------------------ Standard example
queue = []
def length():
    """ Returns number of waiting customers"""
    return len(queue)

def show():
    """ Print list of customers, longest waiting customer at end."""
    for name in queue:
        print("Waiting customer: {}" .format(name))

def add(name):
    """ Customer with name 'name' joining the queue"""
    queue.insert(0, name)

def next():
    """ Returns name of next to serve, removes customer from queue"""
    return queue.pop()

add('Samudero'); add('Fangohr'); add('Takada')
show(); next()