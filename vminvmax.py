import matplotlib.pyplot as plt
import numpy as np

a = np.outer(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
a = (a / a.max() - 0.5) * 5.0

fig, ax = plt.subplots(1, figsize=(10,10))
m = ax.imshow(a, cmap='plasma')
plt.subplots_adjust(top = 1.0, bottom = 0.0, right = 1.0, left = 0.0)
plt.savefig('./CMap_woMinMax.png', dpi=300)
plt.close(fig)
plt.clf()

fig, ax = plt.subplots(1, figsize=(10,10))
m = ax.imshow(a, cmap='plasma', vmin=-4.0, vmax=4.0)
plt.subplots_adjust(top = 1.0, bottom = 0.0, right = 1.0, left = 0.0)
fig.colorbar(m)
plt.savefig('./CMap_wMinMax.png', dpi=300)
plt.show()
