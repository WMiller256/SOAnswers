import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)

ax.set_title("title", rotation=-90, position=(1., 0.5), ha='left', va='center')
plt.savefig('./AxesTitleRotation.png', bbox_inches='tight', dpi=300)
ax.set_ylim([0,10])
plt.show()	
