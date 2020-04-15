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

import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

plt.figure(figsize=(12,3))
x = np.arange('2020-04-03T00:00Z', '2020-04-05T00:30Z', np.random.randint(50, 70), dtype='datetime64[m]')
x = np.delete(x, np.s_[4:10])
x = np.delete(x, np.s_[25:32])
y = np.sin(np.linspace(0, np.pi*2, len(x))*2 + np.random.random(len(x)) - 0.5)
plt.plot(x, y)

dx = np.arange(x[0], x[-1]+60, 60, dtype='datetime64[m]').astype(dt.datetime)
fill = [False if dt.time(8, 0, 0) < t.time() < dt.time(20, 0, 0) else True for t in dx]
plt.tick_params(axis='x', rotation=90)
plt.fill_between(dx, plt.ylim()[0], plt.ylim()[1], where=fill, fc='grey', alpha=0.2)
plt.subplots_adjust(bottom=0.3)
plt.savefig('./conditionalshading.png', bbox_inches='tight', dpi=400)
plt.show()
