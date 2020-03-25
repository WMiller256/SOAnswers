import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import ArtistAnimation, FuncAnimation

n = 150
x = np.linspace(0, np.pi*4, n)
df = pd.DataFrame({'cos(x)' : np.cos(x), 
				   'sin(x)' : np.sin(x),
				   'tan(x)' : np.tan(x),
				   'sin(cos(x))' : np.sin(np.cos(x))})

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
lines = []
artists = [[]]
for ax, col in zip(axs.flatten(), df.columns.values):
	ax.tick_params(labelleft=False, left=False, bottom=False, labelbottom=False)
	lines.append(ax.plot(df[col])[0])
	artists.append(lines.copy())
plt.subplots_adjust(hspace=0, wspace=0, left=0.02, right=0.98, bottom=0.02, top=0.98)
plt.margins(0, 0)

anim = ArtistAnimation(fig, artists, interval=500, repeat_delay=1000, blit=True)
anim.save('./ArtistAnimation.gif', writer='imagemagick')

