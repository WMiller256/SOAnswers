import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(10, 6), dpi=300)
nframes = 25

def animate(i):
	im = plt.imread('frame.'+str(i)+'.png')
	plt.imshow(im)
	plt.axis('off')
	print('\r', '{:3.2f}'.format(float(i) / float(nframes - 1) * 100.0), end='')

anim = FuncAnimation(fig, animate, frames=nframes, interval=(2000.0/nframes))
anim.save('output.gif', writer='imagemagick')
print()

