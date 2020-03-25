import imageio

nframes = 25
files = ['frame.'+str(i)+'.png' for i in range(nframes)]

frames = [imageio.imread(f) for f in files]
imageio.mimsave('output.gif', frames, fps=(nframes / 2.0))


