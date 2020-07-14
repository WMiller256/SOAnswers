# Question: https://stackoverflow.com/questions/62884183

import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", hue="size", palette='RdBu', data=tips)

norm = plt.Normalize(tips['size'].min(), tips['size'].max())
sm = plt.cm.ScalarMappable(cmap="RdBu", norm=norm)
sm.set_array([])

ax.get_legend().remove()
ax.figure.colorbar(sm)

plt.savefig('./SNSColorbar.png', bbox_inches='tight', dpi=300)

plt.show()
