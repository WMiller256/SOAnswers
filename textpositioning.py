import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.style.use('./miller.mplstyle')

dates = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
y = [1,2,3,4,5.8]
df = pd.DataFrame({'X': x, 'Y': y})

fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)
show_point = 5.7
ax.axhline(show_point, ls='dotted')
#ax.annotate(show_point, [ax.get_xticks()[0], show_point], va='bottom', ha='right', color='red')
trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
xticks = ax.get_xticks()
ax.text((xticks[1] - xticks[0]) * 0.05, show_point, color="red", s=show_point, ha="right", va="bottom")

show_point2 = 1.7
ax.axhline(show_point2, ls='dotted')
ax.annotate(show_point2, [ax.get_xticks()[0], show_point2], va='bottom', ha='right', color='red')

plt.savefig('./textpositioning.png', bbox_inches='tight', dpi=400)
plt.show()
