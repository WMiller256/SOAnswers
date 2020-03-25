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
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
				 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
				 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
				 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
				 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
	r, g, b = tableau20[i]
	tableau20[i] = (r / 255., g / 255., b / 255.)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'x' : np.random.random(25), 'y' : np.random.random(25)*5, 'z' : np.random.random(25)*2.5})

df.iloc[:, 1:10].plot(kind='bar', stacked=True)
leg = plt.legend()
df.iloc[:, 0].plot(kind='line', y='x', secondary_y=True)
leg2 = plt.legend()
plt.legend(leg.get_patches()+leg2.get_lines(), [text.get_text() for text in leg.get_texts()+leg2.get_texts()], loc='upper left', fancybox=True, framealpha=1, shadow=True, borderpad=1)
leg.remove()
plt.savefig('./twinxLegend.png', bbox_inches='tight', dpi=300)
