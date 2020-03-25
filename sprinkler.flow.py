import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from math import sin, cos

g = 9.81
rho = 1.225
v0 = 50.0    # This can be initialized as desired, I chose 50 m/s for demonstration
C = 0.5

nframes = 100
ndrops = 10
tend = 8.0
time = np.linspace(0.1, tend, nframes)   # Runtime of 4s chosen arbitrarily
dt = time[1] - time[0]					  # change in time between steps
maxs = [0.0, 0.0]
r = [0.001, 0.0045]						  # This stores the range of radii to be used

# I have implemented a class to store the drops for brevity
class drop:

    def __init__(self, pos, vel, r):
        self.pos = pos
        self.vel = vel
        self.r = r

class sprinkler:
# I implemented this as a class to simplify updating the scatter plot
	def __init__(self):
		self.fig, self.ax = plt.subplots()
		self.drops = [None]*ndrops
		self.maxt = 0.0
		## This step is simply to figure out how far the water drops can travel
		## in order to set the bounds of the plot accordingly
		angles = np.linspace(0, np.pi/2, 90)    # We only need to sample from 0 to pi/2
		for angle in angles:
			m = [drop([0.0, 0.1], [v0*cos(angle), v0*sin(angle)], 0.001),
			     drop([0.0, 0.1], [v0*cos(angle), v0*sin(angle)], 0.0045)]
			for d in m:
			    t = 0.0
			    coef = - 0.5*C*np.pi*d.r**2*rho
			    mass = 4/3*np.pi*d.r**3*1000
			    while d.pos[1] > 0:
			        a = np.power(d.vel, 2) * coef * np.sign(d.vel)/mass
			        a[1] -= g
			        d.pos += (d.vel + a * dt) * dt
			        d.vel += a * dt
			        t += dt
			        if d.pos[1] > maxs[1]:
			            maxs[1] = d.pos[1]
			        if d.pos[0] > maxs[0]:
			            maxs[0] = d.pos[0]
			        if d.pos[1] < 0.0:
			            if t > self.maxt:
			                self.maxt = t
			            break
		for ii in range(ndrops):    # Make some randomly distributed water drops
		    self.drops[ii] = drop([0.0, 0.0], [cos(np.random.random()*np.pi)*v0,
		                     sin(np.random.random()*np.pi)*v0],
		                     np.random.random()*(r[1]-r[0]) + r[0])

		anim = animation.FuncAnimation(self.fig, self.update, init_func=self.setup,
		                               interval=200, frames=nframes)
		anim.save('Sprinkler.gif', fps = 20, writer='imagemagick')

	def setup(self):
	    self.scat = self.ax.scatter([d.pos[0] for d in self.drops],
	                                [d.pos[1] for d in self.drops], marker='.', color='k')
	    self.ax.set_xlim([-maxs[0]*1.15, maxs[0]*1.15])
	    self.ax.set_ylim([0, maxs[1]*1.15])

	    return self.scat,

	def update(self,frame):  # Use set_offsets to move the water drops
	    # Create between 0 and ndrops new drops, but only until tend-maxt
	    if time[frame] < tend - self.maxt*1.1:
	        self.create(np.random.randint(0, ndrops))
	    self.step()          # Advance to the next 'step'
	    self.scat.set_offsets(np.stack([[d.pos[0] for d in self.drops],
	                                    [d.pos[1] for d in self.drops]], 1))

	    return self.scat,

	def create(self, i):
		for ii in range(i):
		    self.drops.append(drop([0.0, 0.0], [cos(np.random.random()*np.pi)*v0,
		                     sin(np.random.random()*np.pi)*v0],
		                     np.random.random()*(r[1]-r[0]) + r[0]))
	def step(self):
	    for ii in range(len(self.drops)):
	        coef = - 0.5*C*np.pi*self.drops[ii].r**2*rho    # Aggregated coefficient
	        mass = 4/3*np.pi*self.drops[ii].r**3*1000
	        a = np.power(self.drops[ii].vel, 2) * coef * np.sign(self.drops[ii].vel)/mass
	        a[1] -= g
	        # Approximate how much the position and velocity would change if we assume
	        # a(t) does not change between t and t+dt
	        self.drops[ii].pos += np.array(self.drops[ii].vel) * dt + 0.5 * a * dt**2
	        self.drops[ii].vel += a * dt
	        if self.drops[ii].pos[1] < 0.0:                # Check if the drop has hit the ground
	            self.drops[ii].pos[1] = 0.0
	            self.drops[ii].vel = [0.0, 0.0]

sprinkler()
