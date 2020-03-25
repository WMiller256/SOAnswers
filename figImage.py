import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
	'some data':[2,0,0,3,2,1,4],
	'other data':[5,1,0,5,2,2,3]
})
logo = plt.imread('A.jpg')
title = 'images'
dpi = 150
fig, ax = plt.subplots(1, dpi=125)
df.plot(kind='bar',x='some data',y='other data', ax=ax)
ax.set_title(title, fontsize=20)
h = logo.shape[1]/fig.bbox.ymax
fig.subplots_adjust(0.05, h, 0.97, 0.93)
ax.figure.figimage(logo, 0, 0, alpha=.15, zorder=1)
ax.figure.figimage(logo, fig.bbox.xmax - logo.shape[0], 0, alpha=.15, zorder=1)
plt.savefig('./FigImages.png', dpi=125)
plt.show()
