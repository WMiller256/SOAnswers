import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.swarmplot(x=tips["total_bill"])
artists = ax.get_children()
offsets = []
for a in artists:
	if type(a) is matplotlib.collections.PathCollection:
		offsets = a.get_offsets()
		break
plt.scatter(offsets[50,0], offsets[50,1], marker='o', color='orange', zorder=10)
plt.savefig('./highlight.png', bbox_inches='tight', dpi=300)
