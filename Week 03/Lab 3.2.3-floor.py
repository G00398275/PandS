# Week 03: Lab 3.2.3 Fun with numbers
# This program takes in a float and outputs a rounded down integer
# Author: Ross Downey

import math

numberTofloor = float(input("Please enter a float number: "))
flooredNumber = math.floor (numberTofloor)

print('{} floored is {}' .format (numberTofloor, flooredNumber))