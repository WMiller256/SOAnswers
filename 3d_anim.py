import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

n = 200
fig = plt.figure(figsize=(16,6))
ax = fig.add_subplot(111, projection='3d')
x, y = np.meshgrid(np.linspace(0, 10, n), np.linspace(0, 10, n))
z = np.zeros_like(x)

graph = ax.plot_surface(x, y, z)
ax.set_title('Frame 0')

def update(i):
	z = np.full_like(x, i)
	plt.cla()
	graph = ax.plot_surface(x, y, z)
	ax.set_xlim([0, 10])
	ax.set_ylim([0, 10])
	ax.set_zlim([0, 10])
	ax.set_title('Frame '+str(i))
	return graph,

anim = animation.FuncAnimation(fig, update, frames=11, interval=500, blit=True)
anim.save('3danim.gif', writer='imagemagick', dpi=150)

