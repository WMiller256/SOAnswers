import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation

n = 500
nf = 100
x = np.linspace(0, np.pi*4, n)
df = pd.DataFrame({'cos(x)' : np.cos(x), 
				   'sin(x)' : np.sin(x),
				   'tan(x)' : np.tan(x),
				   'sin(cos(x))' : np.sin(np.cos(x))})

fig, axs = plt.subplots(2, 2, figsize=(5,5), dpi=50)
lines = []
for ax, col in zip(axs.flatten(), df.columns):
	lines.append(ax.plot([], lw=0.5)[0])
	ax.set_xlim(x[0] - x[-1]*0.05, x[-1]*1.05)
	ax.set_ylim([min(df[col].values)*1.05, max(df[col].values)*1.05])
	ax.tick_params(labelbottom=False, bottom=False, left=False, labelleft=False)
plt.subplots_adjust(hspace=0, wspace=0, left=0.02, right=0.98, bottom=0.02, top=0.98)
plt.margins(1, 1)
c = int(n / nf)
def animate(i):
	if (i != nf - 1):
		for line, col in zip(lines, df.columns):
			line.set_data(x[:(i+1)*c], df[col].values[:(i+1)*c])
	else:
		for line, col in zip(lines, df.columns):
			line.set_data(x, df[col].values)		
	return lines
	
anim = FuncAnimation(fig, animate, interval=2000/nf, frames=nf, repeat_delay=1000, blit=True)
anim.save("./FuncAnimation.gif", writer='imagemagick')
