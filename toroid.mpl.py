#
# toroid.py
#
# William Miller
# Nov 22, 2019
#
# Stack Overflow question: https://stackoverflow.com/questions/59000001/how-to-draw-a-line-behind-a-surface-plot-using-pyplot
#
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('./miller.mplstyle')

fig = plt.figure()
ax = fig.gca(projection='3d')

# theta: poloidal angle | phi: toroidal angle
# note: only plot half a torus, thus phi=0...pi
theta = np.linspace(0, 2.*np.pi, 200)
phi   = np.linspace(0, 1.*np.pi, 200)
theta, phi = np.meshgrid(theta, phi)

# major and minor radius
R0, a = 3., 1.
lw = 0.05

# Cue the unpleasantness - the circle must also be drawn as a toroid
x_circle = (R0 + lw*np.cos(theta)) * np.cos(phi)
y_circle = (R0 + lw*np.cos(theta)) * np.sin(phi)
z_circle = lw * np.sin(theta)
c_circle = np.full_like(x_circle, (1.0, 1.0, 1.0, 1.0), dtype=(float,4))

# Delay meshgrid until after circle construction
x_torus = (R0 + a*np.cos(theta)) * np.cos(phi)
y_torus = (R0 + a*np.cos(theta)) * np.sin(phi)
z_torus = a * np.sin(theta)
c_torus = np.full_like(x_torus, (0.0, 0.5, 1.0, 1.0), dtype=(float, 4))

# Create the bridge, filled with transparency
x_bridge = np.vstack([x_circle[-1,:],x_torus[0,:]])
y_bridge = np.vstack([y_circle[-1,:],y_torus[0,:]])
z_bridge = np.vstack([z_circle[-1,:],z_torus[0,:]])
c_bridge = np.full_like(z_bridge, (0.0, 0.0, 0.0, 0.0), dtype=(float, 4))

# Join the circle and torus with the transparent bridge
X = np.vstack([x_circle, x_bridge, x_torus])
Y = np.vstack([y_circle, y_bridge, y_torus])
Z = np.vstack([z_circle, z_bridge, z_torus])
C = np.vstack([c_circle, c_bridge, c_torus])

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=C, linewidth=0)
ax.view_init(elev=15, azim=270)
ax.set_xlim( -3, 3)
ax.set_ylim( -3, 3)
ax.set_zlim( -3, 3)
ax.set_axis_off()

plt.savefig('./example.png', bbox_inches='tight', dpi=300)
