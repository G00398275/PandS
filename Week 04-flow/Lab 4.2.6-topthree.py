# Week 04: topthree.py, Lab 4.2.2 Flow control loops
# This program generates ten random numbers between 0 and 100,
# prints them out and then prints the top three
# Author: Ross Downey

import random
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100
# Creating list parameters to store and manipulate numbers
numbers = []

for i in range (0,10):
    numbers.append(random.randint(rangeFrom, rangeTo))
print ("{} random numbers\t {}" .format (howMany, numbers)) # printing 10 random numbers between 0-100

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}" .format (topHowMany, topOnes [0:topHowMany]))
# printing out the top 3 three of these random numbers in decreasing order