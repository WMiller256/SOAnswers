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
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.minor.visible'] = True
rcParams['ytick.minor.visible'] = True

pgf_with_latex = {
	"text.usetex": True,
	"pgf.rcfonts": False,
	"pgf.preamble": [
			r'\usepackage{color}'
			r'\usepackage{bm}'
		]
	}
matplotlib.rcParams.update(pgf_with_latex)

# Question: https://stackoverflow.com/questions/61062641/pandas-python-legend-not-showing-all-color-categories

import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'fig' : ["Between 1 to 10C", "20C", "500ML", "1LITRE"], 
				   'Bottles' : [18, 15, 217, 922], 
				   'bottle Avg' : [320.86, 99.81, 449.16, 295.53]})
				   
ax = df.plot(kind='bar', x='Bottles', y='bottle Avg', color=['b', 'orange', 'g', 'r'])
ax.legend(labels=df['fig'].tolist(), handles=ax.patches, fancybox=True, shadow=True)
for p in ax.patches:
    ax.annotate("{:.1f}".format(p.get_height()), xy=(p.get_x() * 1.015, p.get_height() * 1.015))
    
plt.savefig('./pandasbarlegend.png', bbox_inches='tight', dpi=400)
plt.show()
