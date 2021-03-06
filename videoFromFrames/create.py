import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

rcParams.update(rcParamsDefault)
rcParams['figure.figsize'] = 10, 8
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


import matplotlib.pyplot as plt
import numpy as np

n = 500
nframes = 72
x = np.linspace(-np.pi*4, np.pi*4, n)

for i, t in enumerate(np.linspace(0, np.pi*2, nframes)):
	print('\r', '{:3.2f}'.format(float(i) / float(nframes - 1) * 100.0), end='')
	plt.plot(x, np.cos(x + t), color=tableau20[1])
	plt.plot(x, np.sin(2*x - t), color=tableau20[1])
	plt.plot(x, np.cos(x + t) + np.sin(2*x - t), color=tableau20[0])
	plt.gca().tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
	plt.ylim(-2.5,2.5)
	plt.savefig('Sinusoids-'+str(i)+'.png', bbox_inches='tight', dpi=300)
	plt.clf()
	
print()
