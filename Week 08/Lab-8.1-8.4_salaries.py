# Lab 8.1 - 8.4 plotting; salaries.py
# This program generated 10 random salaries that are modified as requested
# Author: Ross Downey

import numpy as np 
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10 # specifying min, max and how many numbers needed

np.random.seed(1) # ensures "random" array called is the same each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000 # adding 5000 to each salary in original array
print (salariesPlus)

salariesMult = salaries * 1.05 # multiplying original salaries by 1.05 to increase by 5%
print(salariesMult)
# As this array is a float it is better to convert to an array, the below gives a floor
newSalaries = salariesMult.astype(int)
print(newSalaries)


