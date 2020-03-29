from matplotlib import pyplot as plt
import numpy as np

plt.tricontourf(np.random.uniform(1, 10, 100), np.random.uniform(1, 10, 100), np.random.uniform(1e-6, 1e-5, 100))
cbar = plt.colorbar()
plt.gca().ticklabel_format(useMathText=True)
plt.show()
