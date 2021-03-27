# Lab 9 Errors, Testing and Logging; myfunctions.py
# This program contains the tests for checking useFib.py
# Author: Ross Downey

import logging
#logging.basicConfig (level = logging.DEBUG)

def fibonacci (number):
    a = 0
    b = 1
    fibonacciSequence = [0]  # one in list already, number -1 times
    
    for i in range (1,number):
        fibonacciSequence.append(b)
        a, b = b, a + b
    #logging.debug ("%d: %s", number, fibonacciSequence)
    if number == 0:
        return[]
    if number < 0:
        raise ValueError ('number must be > 0')


if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci (0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'
try:
    fibonacci(-1)
except ValueError:
    pass
else: 
    assert False, 'fibonacci missing ValueError'
print ("All Good")

