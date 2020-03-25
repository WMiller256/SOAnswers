import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
gs = fig.add_gridspec(2, 9)

# Qury image
ax1 = fig.add_subplot(gs[:, 0])
#Positive image
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[0, 3])
ax5 = fig.add_subplot(gs[0, 4])
# Negative images
ax6 = fig.add_subplot(gs[1, 1])
ax7 = fig.add_subplot(gs[1, 2])
ax8 = fig.add_subplot(gs[1, 3])
ax9 = fig.add_subplot(gs[1, 4])

for a in fig.get_axes():
	a.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)

plt.savefig('./GridSpec.png', bbox_inches='tight', dpi=300)
plt.show()
