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


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

dates = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
y = [1,2,3,4,5.8]
df = pd.DataFrame({'X': dates, 'Y': y})

fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)
show_point = 5.7
ax.axhline(show_point, ls='dotted')
ax.annotate(show_point, [ax.get_xticks()[0], show_point], va='bottom', ha='right', color='red')

show_point2 = 1.7
ax.axhline(show_point2, ls='dotted')
ax.annotate(show_point2, [ax.get_xticks()[0], show_point2], va='bottom', ha='right', color='red')

plt.savefig('./textpositioning.png', bbox_inches='tight', dpi=400)
plt.show()
