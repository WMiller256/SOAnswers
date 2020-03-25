import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.patches as patches
import numpy as np

class SnaptoCursor(object):
	def __init__(self, ax):
		ax.figure.canvas.draw()
		self.ax = ax
		self.bg = ax.figure.canvas.copy_from_bbox(ax.bbox)
		self.lx = ax.axhline(color='r', lw=1)  # the horiz line
		self.ly = ax.axvline(color='r', lw=1)  # the vert line
		self.x = 0
		self.y = 0

	def mouse_move(self, event):
		if not event.inaxes:
			return
		x, y = event.xdata, event.ydata
		# update the line positions
		self.lx.set_ydata(y)
		self.ly.set_xdata(x)
		ax.figure.canvas.restore_region(self.bg)
		self.ax.draw_artist(self.lx)
		self.ax.draw_artist(self.ly)
		self.ax.figure.canvas.blit(self.ax.figure.bbox)

img = image.imread("image.jpg")
fig,ax =plt.subplots(1)
ax.imshow(img)

snap_cursor = SnaptoCursor(ax)
fig.canvas.mpl_connect('motion_notify_event', snap_cursor.mouse_move)

plt.show()
