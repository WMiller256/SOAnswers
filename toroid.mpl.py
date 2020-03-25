#
# toroid.py
#
# William Miller
# Nov 22, 2019
#
# Stack Overflow question: https://stackoverflow.com/questions/59000001/how-to-draw-a-line-behind-a-surface-plot-using-pyplot
#

import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

rcParams.update(rcParamsDefault)
rcParams['figure.figsize'] = 6, 4
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = 16
rcParams['figure.dpi'] = 100
rcParams['savefig.dpi'] = 300
rcParams['figure.titlesize'] = 28
rcParams['legend.fontsize'] = 16
rcParams['ytick.labelsize'] = 14
rcParams['xtick.labelsize'] = 14
rcParams['axes.labelsize'] = 20
rcParams['lines.dash_capstyle'] = 'round'
rcParams['lines.linestyle'] = 0.01,1.5
rcParams['lines.linewidth'] = 3
rcParams['axes.titlepad'] = 10.0

pgf_with_latex = {
	"text.usetex": True,
	"pgf.rcfonts": False,
	"pgf.preamble": [
			r'\usepackage{color}'
			r'\usepackage{bm}'
		]
	}
matplotlib.rcParams.update(pgf_with_latex)

# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
				 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
				 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
				 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
				 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
	r, g, b = tableau20[i]
	tableau20[i] = (r / 255., g / 255., b / 255.)


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
