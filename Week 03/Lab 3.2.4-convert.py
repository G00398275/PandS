# Week 03: Lab 3.2.4 Fun with numbers
# This program takes in an input of dollars and cents in float
# and outputs the absolute amount in cent 
# Author: Ross Downey
import math

dollarsAndCents = float (input("Please enter the amount in dollars and cents as a float: "))
centsUnrounded = abs(dollarsAndCents * 100)
centsRounded = round(centsUnrounded)


print ('The amount in cents is {}' .format (centsRounded))