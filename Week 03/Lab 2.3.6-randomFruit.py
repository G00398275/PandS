# Week 03: Lab 2.3.6 Variables and State
# This program prints out a random fruit using a list method
# Author: Ross Downey

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear', 'Kiwi']

# we want a random number between 0 and length -1
index = random.randint (0,len(fruits)-1)

fruit = fruits[index]
print("This is a Random Fruit: {}" .format(fruit))