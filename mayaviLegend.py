import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import mayavi.mlab as mlab
from mayavi.api import OffScreenEngine
import numpy as np

plt.style.use('miller')

cycler = plt.gca()._get_lines.prop_cycler
colors = [next(cycler)['color'] for i in range(4)]

mlab.options.offscreen = True
e = OffScreenEngine()
e.start()
fig = mlab.figure(engine=e, size=(5000,5000), fgcolor=(0,0,0), bgcolor=(1,1,1))
mlab.view(azimuth=45, elevation=0)

n = 500
d = np.linspace(0, np.pi*8, n)

mlab.plot3d(d, np.cos(d**1.2), np.cos(d), color = colors[0])
mlab.plot3d(d, np.sin(d), np.sin(d), color = colors[1])
mlab.plot3d(d, np.sin(d)*np.cos(d), np.cos(d), color = colors[2])
mlab.plot3d(d, np.sin(d)**2, np.sin(d)**2, color = colors[3])

mlab.savefig("./example.png")

im = plt.imread("./example.png")
labels = ["One", "Two", "Three", "Four"]

elements = [Line2D([0], [0], label = l, color = c) for l, c in zip(labels, colors[:4])]
plt.imshow(im)
plt.legend(handles = elements)
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.savefig("./example.png")
