# Question: https://stackoverflow.com/questions/61062641/pandas-python-legend-not-showing-all-color-categories

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('miller')

df = pd.DataFrame({'fig' : ["Between 1 to 10C", "20C", "500ML", "1LITRE"], 
				   'Bottles' : [18, 15, 217, 922], 
				   'bottle Avg' : [320.86, 99.81, 449.16, 295.53]})
				   
ax = df.plot(kind='bar', x='Bottles', y='bottle Avg', color=['b', 'orange', 'g', 'r'])
ax.legend(labels=df['fig'].tolist(), handles=ax.patches, fancybox=True, shadow=True)
for p in ax.patches:
    ax.annotate("{:.1f}".format(p.get_height()), xy=(p.get_x() * 1.015, p.get_height() * 1.015))
    
plt.savefig('./pandasbarlegend.png', bbox_inches='tight', dpi=400)
plt.show()
