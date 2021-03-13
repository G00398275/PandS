# Lab 8.13; hurling.py
# This program plots the roll call of All-Ireland hurling winners
# Author: Ross Downey

import numpy as np
import matplotlib.pyplot as plt

numberOfWins = np.array([36,30,28,9,6,6,5])
winners = ["Kilkenny", "Cork", "Tipperary", "Limerick", "Dublin", "Wexford", "Galway"]
myExplode = [0.1, 0, 0, 0, 0, 0, 0,]
myColours = ["black", "red", "blue", "green", "cornflowerblue", "yellow", "maroon"]

plt.pie (numberOfWins, labels = winners, startangle = 90, explode = myExplode,
shadow = True, colors = myColours)
plt.legend (title = "Hurling All-Ireland Role of Honour")
plt.show()