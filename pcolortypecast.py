import numpy as np
from matplotlib import pyplot as plt

x = [0, 1]
y = [0, 2]
val = [[1]]
xx, yy = np.meshgrid(x, y)

xx = xx.astype('float64')
yy = yy.astype('float64')

fig, ax = plt.subplots(1, 2, figsize=[10, 10])

ax = plt.subplot(2, 1, 1)
yy[1,0] = 2.9
ax.pcolor(xx, yy, val, edgecolors='black')

ax = plt.subplot(2, 1, 2)
yy[1,0] = 3
ax.pcolor(xx, yy, val, edgecolors='black')
plt.savefig('./pcolor.png', bbox_inches='tight', dpi=300)
