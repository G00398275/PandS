# This program tests the myFunctions.py program
# Author: Ross Downey

import myFunctions as mf


import logging

def fibonacci (number):
    a = 0
    b = 1
    fibonacciSequence = [0]  # one in list already, number -1 times
    
    for i in range (1,number):
        fibonacciSequence.append(b)
        a, b = b, a + b
    logging.debug ("%d: %s", number, fibonacciSequence)
    if number == 0:
        return[]
    if number == 0:
        return []

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci (0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'