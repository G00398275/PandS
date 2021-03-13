# Lab 8.7; scatter.py
# This program plots a scatter plot of the salaries in salaries.py overlayed with y=xSquared
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
# plt.show()
# commented out first plot until y = xSquared plot is added

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # giving x squared

plt.plot(xpoints, ypoints, color = 'r', label = "X Squared") # defining colour and label

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend() # adding title, axis labels and legend
#plt.show() # for showing plot 

# or can save to a new file
plt.savefig('prettier-plot.png')