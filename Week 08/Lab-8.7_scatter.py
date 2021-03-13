# Lab 8.7; scatter.py
# This program plots a scatter plot of the salaries in salaries.py
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10 # specifying min, max and how many numbers needed

np.random.seed(1) # ensures "random" array called is the same each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 21, high = 65,size = numberOfEntries)

plt.scatter(ages,salaries) # scatter plot is random
plt.show()