import numpy as np
import mayavi.mlab as mlab
from mayavi.api import OffScreenEngine
mlab.options.offscreen = True

# theta: poloidal angle | phi: toroidal angle
# note: only plot half a torus, thus phi=0...pi
theta = np.linspace(0, 2.*np.pi, 720)
phi   = np.linspace(0, 1.*np.pi, 720)

# major and minor radius
R0, a = 3., 1.

x_circle = R0 * np.cos(phi)
y_circle = R0 * np.sin(phi)
z_circle = np.zeros_like(x_circle)

# Delay meshgrid until after circle construction
theta, phi = np.meshgrid(theta, phi)
x_torus = (R0 + a*np.cos(theta)) * np.cos(phi)
y_torus = (R0 + a*np.cos(theta)) * np.sin(phi)
z_torus = a * np.sin(theta)

mlab.figure(bgcolor=(1.0, 1.0, 1.0), size=(2000,2000))
mlab.view(azimuth=90, elevation=105)

mlab.plot3d(x_circle, y_circle, z_circle)
mlab.mesh(x_torus, y_torus, z_torus, color=(0.0, 0.5, 1.0))
mlab.savefig("./example.png")

