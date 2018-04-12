# Dictionaries [184]
# also called "associative arrays" and "hash tables"
# are "unordered" sets of key-value pairs

"""
Created on Wed 22 Mar 2018
@author: pandus
"""

# ------------------------ Examples
d = {}                      # an empty dictionary

d['today'] = '22 deg C'     # 'today' is key
                            # '22 deg C' is value

d['yesterday'] = '19 deg C'

d.keys()                    # returns a list of all keys

print (d['today'])          # returns '22 deg C'

# ------------------------ Examples
order = {}                  # create empty dictionary

# add orders as they come in
order['Peter']  = 'Pint of bitter'
order['Paul']   = 'Half pint of Hoegarden'
order['Mary']   = 'Gin Tonic'

# deliver order at bar
for person in order.keys():
    print("{} request {}" .format(
        person, order[person]))

# ------------------------ Another Examples
dic    = {}
dic["Andy C"]   = "room 1031"
dic["Ken"]      = "room 2017"
dic["Hans"]     = "room 1033"

for key in dic.keys():
    print("{} works in {}"
          .format(key, dic[key]))

# ------------------------ Without dictionary:
people  = ["Hans", "Andy C", "Ken"]
rooms   = ["room 1033", "room 1031", "room 1027"]

# possible inconsistency here since we have two lists
if not len(people) == len(rooms):
    raise ValueError("people and rooms" +
                     "differ in length")

for i in range(len(rooms)):
    print("{} works in {}" .format(people[i], rooms[i]))

# ------------------------ Iterating over dictionaries:
order = {}                  # create empty dictionary

order['Peter']      = 'Pint of bitter'
order['Paul']       = 'Half pint of Hoegarden'
order['Mary']       = 'Gin Tonic'

# iterating over keys:
for person in order.keys():
    print(person, "request", order[person])

# is equivalent to iterating over the dictionary:
for person in order:
    print(person, "requests", order[person])