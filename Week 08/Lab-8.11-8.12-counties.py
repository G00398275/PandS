# Lab 8.11-8.12; counties.py
# This program plots pie and bar charts of a list of counties
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Mayo', 'Galway', 'Roscommon', 'Dublin', 'Donegal', 'Waterford']
# Array of counties
counties = np.random.choice(
    possibleCounties ,
    p = [0.1, 0.3, 0.2, 0.12, 0.15, 0.13],
    size = (100)
)#  100 randomly picked from array, frequency set by p values

# need no. of occurrences of each county
# return a tuple of unique values and how many times they appear
unique, counts = np.unique(counties, return_counts = True)
# This is now put into a pie plot
#plt.pie(counts, labels = unique)
#plt.show()

plt.bar(unique, counts) # or add to a bar chart
plt.show()