import matplotlib.pyplot as plt
import itertools
import numpy as np

plt.style.use('./miller.mplstyle')

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
