import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

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

rcParams.update(rcParamsDefault)
rcParams['axes.prop_cycle'] = matplotlib.cycler(color=tab20)
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

import matplotlib.pyplot as plt
import itertools
import numpy as np

def gettime(s):
	e = ["".join(x) for _, x in itertools.groupby(s, key=str.isdigit)]
	h = float(e[e.index("h") - 1]) if "h" in e else 0.0
	m = float(e[e.index("m") - 1]) if "m" in e else 0.0
	s = float(''.join(e[e.index("s") - 3:e.index("s")])) if "s" in e else 0.0

	return 3600 * h + 60 * m + s

lines = []
with open("log.txt") as fp:
	lines = fp.read().splitlines()

files = []
idx = 0
keys = ["A", "b1", "b2", "b3"]
methods = []
while idx < len(lines):
	if ".mp4" in lines[idx]:
		method = {k : 0.0 for k in keys}
		files.append(lines[idx].split(' ')[0])
		idx += 1
		while idx < len(lines) and ".mp4" not in lines[idx]:
			if "Method" in lines[idx]:
				substrings = list(filter(None, lines[idx].split(' ')))
				if substrings[-1] in keys:
					while "real" not in lines[idx]:
						idx += 1
					method[substrings[-1]] = gettime(lines[idx].split(' ')[-1])
			idx += 1
		methods.append(method)
	else:
		idx += 1

data = np.zeros((len(keys), len(files)))
for idx, (d, f) in enumerate(zip(methods, files)):
	data[:,idx] = np.array([d[k] for k in keys]).reshape(data[:,idx].shape)

x = np.arange(len(files))
w = (1.0 / data.shape[0]) * 0.6
names = ["A", "B, b1", "B, b2", "B, b3"]
for i in range(data.shape[0]):
	plt.bar(x - w * i, data[i,:], width=w, label=names[i])

plt.tick_params(bottom = False)
plt.xticks(x - w * (i - 1.5), files)
plt.legend(title="Method")
plt.savefig('./ffmpegBenchmark.png', bbox_inches='tight', dpi=300)
plt.show()
