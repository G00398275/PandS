# Lab 8.14; normalRandom.py
# This program generates a random, normalized histogram
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(45, 5, 4000)
# 45 = value histogram is concentrated around
# 5 = standard deviation around the mean
# 4000 = frequency
plt.hist(x)
plt.show()
