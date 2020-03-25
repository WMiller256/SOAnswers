import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

rcParams.update(rcParamsDefault)
rcParams['figure.figsize'] = 14, 9
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
#rcParams['lines.linestyle'] = 0.01,1.5
rcParams['lines.linewidth'] = 1
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
tab20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
				 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
				 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
				 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
				 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tab20)):
	r, g, b = tab20[i]
	tab20[i] = (r / 255., g / 255., b / 255.)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import mayavi.mlab as mlab
from mayavi.api import OffScreenEngine
import numpy as np

colors = tab20

mlab.options.offscreen = True
e = OffScreenEngine()
e.start()
fig = mlab.figure(engine=e, size=(5000,5000), fgcolor=(0,0,0), bgcolor=(1,1,1))
mlab.view(azimuth=45, elevation=0)

n = 500
d = np.linspace(0, np.pi*8, n)

mlab.plot3d(d, np.cos(d**1.2), np.cos(d), color = colors[0])
mlab.plot3d(d, np.sin(d), np.sin(d), color = colors[1])
mlab.plot3d(d, np.sin(d)*np.cos(d), np.cos(d), color = colors[2])
mlab.plot3d(d, np.sin(d)**2, np.sin(d)**2, color = colors[3])

mlab.savefig("./example.png")

im = plt.imread("./example.png")
labels = ["One", "Two", "Three", "Four"]

elements = [Line2D([0], [0], label = l, color = c) for l, c in zip(labels, colors[:4])]
plt.imshow(im)
plt.legend(handles = elements)
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.savefig("./example.png")
