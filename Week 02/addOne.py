# Week 02 ; addOne.py, Lab 2.2 First Programs
# This program reads a number and prints out one more than that number
# Author: Ross Downey

number = int(input ('Please enter a number:')) # asks for a number from user (ensuring it is an integer)
newNumber = number + 1 # creates a new number + 1 to the original number entered

print ('{} plus one is {}' .format (number, newNumber)) # prints number plus one is newNumber