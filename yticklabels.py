import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 2, figsize=(12,6))
axs[0].set_yticklabels(np.linspace(0, 10, len(axs[0].get_yticks())))
plt.savefig('./YTickLabels.png', bbox_inches='tight', dpi=300)
plt.show()
