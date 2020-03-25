import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

rcParams.update(rcParamsDefault)
rcParams['figure.figsize'] = 12, 9
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
rcParams['lines.linewidth'] = 2
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

import shapely.geometry as geom
from shapely import affinity
import matplotlib.pyplot as plt
import numpy as np

n = 360
theta = np.linspace(0, np.pi*2, n)

a = 2
b = 1
angle = 45.0

r = a * b  / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)
xy = np.stack([r * np.cos(theta), r * np.sin(theta)], 1)

ellipse = affinity.rotate(geom.Polygon(xy), angle, 'center')

x, y = ellipse.exterior.xy
plt.plot(x, y, lw = 1, color='k')
ng = 50
rnd = np.array([[ii, jj] for ii in np.linspace(min(x),max(x),ng) for jj in np.linspace(min(y),max(y),ng)])

res = np.array([p for p in rnd if ellipse.contains(geom.Point(p))])

plt.scatter(rnd[:,0], rnd[:,1], s = 50, color=tableau20[1])
plt.scatter(res[:,0], res[:,1], color=tableau20[0], s = 15)
plt.savefig('./EllipseContains.png', bbox_inches='tight', dpi=300)
plt.show()
