# Week 03: Lab 2.3.4 Variables and State
# This program ouptputs a random number between 1 and 10
# Author: Ross Downey

import random

min = int(input ("Please enter the minimum range number:"))
max = int(input ("Please enter the maximum range number:"))

number = random.randint (min, max)
print ("This is a random number: {}" .format (number))