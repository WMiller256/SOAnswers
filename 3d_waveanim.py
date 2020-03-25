import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

n = 200
fig = plt.figure(figsize=(16,6))
ax = fig.add_subplot(111, projection='3d')
yy, zz = np.meshgrid(np.linspace(-1,1), np.linspace(-1,1))

def update(i):
	i *= 22
	p = np.zeros((3, n*4))
	p[0,:] = np.linspace(-np.pi*16, np.pi*16, n*4)
	x = p[0,i:i+n*2]
	p[1,i:i+n*2] = np.sin(2*x + np.pi/2) * np.sin(x/16 + np.pi/2)/2
	p[2,i:i+n*2] = np.sin(2*x) * np.cos(x/16)/2
	plt.cla()
	ax.set_xlim([-np.pi*16, np.pi*16])
	ax.set_ylim([-1,1])
	ax.set_zlim([-1,1])
	ax.plot_surface(np.full_like(yy, -np.pi*16), yy, zz, color='b', alpha=0.2)
	ax.plot_surface(np.full_like(yy, np.pi*16), yy, zz, color='b', alpha=0.2)
	plot, = ax.plot(p[0,:], p[1,:], p[2,:], color='red', lw=1)
	return plot,

anim = animation.FuncAnimation(fig, update, frames=n//10, interval=2000/(n//10))
anim.save('wavefunc.gif', writer='imagemagick')

