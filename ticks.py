import matplotlib.pyplot as plt
import numpy as np

plt.figure()

x = np.linspace(0, 10, 25)
y = np.random.uniform(1.3, 1.7, 25)
plt.subplot(211)
plt.scatter(x, y)
plt.locator_params(axis='y', nbins=8)

plt.subplot(212)
plt.scatter(x, y)
plt.ylim([min(y), max(y)])
plt.locator_params(axis='y', nbins=8)
plt.ylim([plt.yticks()[0][0], plt.yticks()[0][-1]])
plt.show()
