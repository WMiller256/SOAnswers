import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('miller')

df = pd.DataFrame({'x' : np.random.random(25), 'y' : np.random.random(25)*5, 'z' : np.random.random(25)*2.5})

df.iloc[:, 1:10].plot(kind='bar', stacked=True)
leg = plt.legend()
df.iloc[:, 0].plot(kind='line', y='x', secondary_y=True)
leg2 = plt.legend()
plt.legend(leg.get_patches()+leg2.get_lines(), [text.get_text() for text in leg.get_texts()+leg2.get_texts()], loc='upper left', fancybox=True, framealpha=1, shadow=True, borderpad=1)
leg.remove()
plt.savefig('./twinxLegend.png', bbox_inches='tight', dpi=300)
