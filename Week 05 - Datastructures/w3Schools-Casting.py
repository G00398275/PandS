# Practicing casting, examples in https://www.w3schools.com/python/python_casting.asp
# Author: Ross Downey

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# despite the originals being floats / strings the int command before the bracket casts it as an int

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# same here, all being casted as floats

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# all being casted as strings