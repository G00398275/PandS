# Week 03: Lab 2.3.7 Variables and State
# This program demonstrates how to fix concatenation error between strings and integers
# Author: Ross Downey

#message = 'I have eaten ' + 99 + ' burritos'
#print (message)

numberOfBurritos = (99) # conversion of integer to string for concatenation

message = ("I have eaten + {} + burritos " .format (numberOfBurritos))
print (message)

#eggs is a valid variable name and 100 isn't as 100 is an integer while eggs is a string

# Three functions are:
int
float
str