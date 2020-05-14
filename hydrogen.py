# Question: https://stackoverflow.com/questions/61697682/
import numpy as np
from scipy.special import sph_harm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import cmath


#Create Diagramm
fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111, projection='3d')

#Variables
l = 0
m = 0
phi = np.linspace(0, np.pi , 150)
theta = phi = np.linspace(0, 2*np.pi , 150)

#Variables for linear combination
l2 = 1
m2 = 0
t = 0
nframes = 36
surf = ax.plot_surface(np.array([[]]), np.array([[]]), np.array([[]]))
ax.set_xlim([-0.75, 0.75])
ax.set_ylim([-0.75, 0.75])
ax.set_zlim([-0.75, 0.75])

#Calculate  linear combination
def animate(i):
	global surf
	print(i)
	t = 2 * np.pi / nframes * i;
	X = abs(sph_harm(m, l, theta, phi)  + sph_harm(m2, l2, theta, phi) * cmath.exp(-t*1j)) * \
	    np.outer(np.cos(phi), np.sin(theta))
	Y = abs(sph_harm(m, l, theta, phi)  + sph_harm(m2, l2, theta, phi) * cmath.exp(-t*1j)) * \
	    np.outer(np.sin(phi), np.sin(theta))
	Z = abs(sph_harm(m, l, theta, phi)  + sph_harm(m2, l2, theta, phi) * cmath.exp(-t*1j)) * \
	    np.outer(np.ones(np.size(phi)), np.cos(theta))

	surf.remove()
	fig.canvas.draw()
	surf = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='b')

anim = FuncAnimation(fig, animate, frames=nframes+1, interval=2000/(nframes+1))
anim.save('./hydrogen.gif', writer='imagemagick')
