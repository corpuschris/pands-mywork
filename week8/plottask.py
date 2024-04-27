#This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a lot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

#Author: Christiano Ferreira

import numpy as np
import matplotlib.pyplot as plt

# Generatingrandom data for normal distribution
data = np.random.normal (5, 2, 1000)

# Generate x values 0 to 10

x_values = np.linspace(0, 10, 100)

#Calculate h(x)=x3

h_values = x_values ** 3

#Plotting histogram

plt.hist(data, bins = 30, density = True)

#Plotting h(x)=x3 in red

plt.plot(x_values, h_values, 'r-')

# Displaying plot

plt.show()