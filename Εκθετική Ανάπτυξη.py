import numpy as np
import matplotlib.pyplot as plt

#
# P(t) = P0 * e^(r*t)
P0 = 1000  
r = 0.05   
t = np.array([0, 1, 2, 3, 4, 5]) 


population = P0 * np.exp(r * t)
print("Years:", t)
print("Population:", population.astype(int))

growth_rate = (population[1:] - population[:-1]) / population[:-1] * 100
print("Growth rate (%):", growth_rate.round(2))