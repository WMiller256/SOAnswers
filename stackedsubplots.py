
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')

mp = PdfPages('multipage.pdf')

mp.savefig(fig)
mp.close()
