# Question: https://stackoverflow.com/questions/61472204
import matplotlib.pyplot as plt
import numpy as np
import math

h = 6.62607015e-34
k = 1.380649e-23
c = 299792458.00
sb = (2 * math.pi**5 * k**4) / (15 * c**2 * h**3)

def one_star():
	mass = np.random.uniform(0.1, 50)
	radius = mass**0.9 * 6.96e8
	B = np.random.uniform(3.3, 3.7)
	luminosity = mass**B * 3.828e26
	sa = 4 * math.pi * radius**2
	T = (luminosity / (sa * sb))**(1/4)
	x = np.linspace(1e-8, 1e-6, 1000)
	I = ((2 * h * c**2) / x**5) * (1 / (np.exp((h * c) / (x * k * T)) - 1))
	plt.plot(x, I)

for i in range(5):
	one_star()
plt.savefig('./blackbody.png', bbox_inches='tight', dpi=400)
plt.show()
