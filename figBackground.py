import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np

plt.style.use('miller')

x = np.linspace(0, np.pi*4, 100)

fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(np.sin(x)))
fig.patch.set_facecolor((0.68, 0.78, 0.91))
plt.gca().patch.set_alpha(0.7)

plt.savefig('./FigBackground.png', bbox_inches='tight', dpi=300, facecolor = fig.get_facecolor())
