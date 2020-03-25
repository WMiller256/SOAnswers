import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

color_list = [(.14,.33,.49), (.08,.41,.27), (.37,.76,.35), (.92,.58,.13),
              (.90,.25,.09), (.96,.75,.12), (.74,.09,.15), (.80,.76,.56), 
              (.56,.70,.72), (.77,.71,.76)]

t = np.linspace(0, np.pi*2, 72)
circle_list = [Circle((r * 2, 0), r, antialiased=False, facecolor=color) for r, color in zip(np.linspace(1, 4, 10), color_list)]

fig = plt.figure(figsize=(4,4))
ax = plt.gca()
ax.set_aspect('equal')

for i in range(10):
	circle = circle_list[i]
	ax.add_patch(circle)

plt.savefig('test.png', dpi=350)
tmp = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
arr = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
arr = arr.reshape(fig.canvas.get_width_height()[::-1] + (3,))
np.save('arr.npy', arr)

circles_npy = np.load('./arr.npy')
