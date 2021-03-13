# Lab 8.5; yEqualsXSquared.py
# This program plots the function y = x squared
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # giving x squared

plt.plot(xpoints,ypoints)
plt.show()

