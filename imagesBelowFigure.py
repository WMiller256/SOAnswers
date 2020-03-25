import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def add_image(axe, filename, position, zoom):
	img = plt.imread(filename)
	off_img = matplotlib.offsetbox.OffsetImage(img, zoom = zoom, resample = False)
	art = matplotlib.offsetbox.AnnotationBbox(off_img, position, xybox = (0, 0),
			xycoords = axe.transAxes, boxcoords = "offset points", frameon = False)
	axe.add_artist(art)

fig = plt.figure(dpi=1000)
axe = plt.axes()
fig.set_size_inches(3, 1.5)
axe.plot(np.arange(10), np.arange(10))

add_image(axe, "A.jpg", position = (0.2, 0.7), zoom = 0.07)

fig.savefig("temp.pdf", bbox_inches = "tight", pad_inches = 0)
plt.show()
