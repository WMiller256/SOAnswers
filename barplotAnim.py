import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import array

val = array([array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]),
array([ 0.       , -1.       , -1.25     , -1.3125   , -1.       ,
-1.5      , -1.6875   , -1.75     , -1.25     , -1.6875   ,
-1.84375  , -1.8984375, -1.3125   , -1.75     , -1.8984375,
0.       ]),
array([ 0.        , -1.9375    , -2.546875  , -2.73046875, -1.9375    ,
-2.8125    , -3.23828125, -3.40429688, -2.546875  , -3.23828125,
-3.56835938, -3.21777344, -2.73046875, -3.40429688, -3.21777344,
0.        ]),
array([ 0.        , -2.82421875, -3.83496094, -4.17504883, -2.82421875,
-4.03125   , -4.7097168 , -4.87670898, -3.83496094, -4.7097168 ,
-4.96374512, -4.26455688, -4.17504883, -4.87670898, -4.26455688,
0.        ]),
array([ 0.        , -3.67260742, -5.0980835 , -5.58122253, -3.67260742,
-5.19116211, -6.03242493, -6.18872833, -5.0980835 , -6.03242493,
-6.14849091, -5.15044403, -5.58122253, -6.18872833, -5.15044403,
0.        ])])

def barlist(n): 
	return val[n]

fig=plt.figure()
n=100 #Number of frames
x=range(16)
ylim = [-10, 0]
barcollection = plt.bar(x, barlist(0))
plt.ylim(ylim)

def animate(i):
	y = barlist(i+1)
	plt.cla()
	bar = plt.gca().bar(x, barlist(i))
	plt.ylim(ylim)
	return bar

anim=animation.FuncAnimation(fig,animate, blit=True, repeat=False, frames=4)
anim.save('movie.1.mp4', writer=animation.FFMpegWriter(fps=1))

def animate(i):
	global barcollection
	y = barlist(i+1)
	for i, b in enumerate(barcollection):
		b.set_height(y[i])
	fig.canvas.draw()
	return barcollection
            
anim=animation.FuncAnimation(fig,animate, blit=True, repeat=False, frames=4)
anim.save('movie.2.mp4', writer=animation.FFMpegWriter(fps=1))
