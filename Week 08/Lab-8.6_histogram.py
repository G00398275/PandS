# Lab 8.6; histogram.py
# This program plots a histogram of the salaries in salaries.py
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10 # specifying min, max and how many numbers needed

np.random.seed(1) # ensures "random" array called is the same each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()