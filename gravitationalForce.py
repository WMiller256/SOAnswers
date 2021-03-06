import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as geom

plt.style.use('./miller.mplstyle')

def centerOfMass(r, density = 1.0, n = 100):
	theta = np.linspace(0, np.pi*2, len(r))
	xy = np.stack([np.cos(theta)*r, np.sin(theta)*r], 1)

	mass_dist = geom.Polygon(xy)
	x, y = mass_dist.exterior.xy

	# Create the grid and populate with polygons
	gx, gy  = np.meshgrid(np.linspace(min(x), max(x), n), np.linspace(min(y), max(y), n))
	polygons = [geom.Polygon([[gx[i,j],    gy[i,j]], 
							  [gx[i,j+1],  gy[i,j+1]], 
							  [gx[i+1,j+1],gy[i+1,j+1]], 
							  [gx[i+1,j],  gy[i+1,j]],
							  [gx[i,j],    gy[i,j]]])
				for i in range(gx.shape[0]-1) for j in range(gx.shape[1]-1)]

	# Calculate center of mass
	R = np.zeros(2)
	M = 0
	for p in polygons:
		m = (p.intersection(mass_dist).area / p.area) * density
		M += m
		R += m * np.array([p.centroid.x, p.centroid.y])

	return geom.Point(R / M), M

density = 1.0     # kg/m^2
G = 6.67408e-11   # m^3/kgs^2
theta = np.linspace(0, np.pi*2, 100)
r = np.cos(theta*2+np.pi)+5+np.sin(theta)+np.cos(theta*3+np.pi/6)

R, M = centerOfMass(r, density)
m = geom.Point(20, 0)
r_1 = m.distance(R)
m_1 = 5.0         # kg
F = G * (m_1 * M) / r_1**2
rhat = np.array([R.x - m.x, R.y - m.y])
rhat /= (rhat[0]**2 + rhat[1]**2)**0.5

plt.figure(figsize=(12, 6))
plt.axis('off')
plt.plot(np.cos(theta)*r, np.sin(theta)*r, color='k', lw=0.5, linestyle='-')
plt.scatter(m.x, m.y, s=20, color='k')
plt.text(m.x, m.y-1, r'$m$', ha='center')
plt.text(1, -1, r'$M$', ha='center')
plt.quiver([m.x], [m.y], [rhat[0]], [rhat[1]], width=0.004, scale=0.25, scale_units='xy')
plt.text(m.x - 5, m.y + 1, r'$F = {{{:.5e}}}$'.format(F))
plt.scatter(R.x, R.y, color='k')
plt.text(R.x, R.y+0.5, 'Center of Mass', va='bottom', ha='center')
plt.gca().set_aspect('equal')
plt.savefig('./GravitationalForceDiagram.png', bbox_inches='tight', dpi=300)

class pointMass:
	def __init__(self, mass, x, y):
		self.mass = mass
		self.x = x
		self.y = y

density = 1.0     # kg/m^2
G = 6.67408e-11   # m^3/kgs^2

def netForce(r, m1, density = 1.0, n = 100):
	theta = np.linspace(0, np.pi*2, len(r))
	xy = np.stack([np.cos(theta)*r, np.sin(theta)*r], 1)

    # Create a shapely polygon for the mass distribution
	mass_dist = geom.Polygon(xy)
	x, y = mass_dist.exterior.xy

	# Create the grid and populate with polygons
	gx, gy  = np.meshgrid(np.linspace(min(x), max(x), n), np.linspace(min(y), max(y), n))
	polygons = [geom.Polygon([[gx[i,j],    gy[i,j]], 
							  [gx[i,j+1],  gy[i,j+1]], 
							  [gx[i+1,j+1],gy[i+1,j+1]], 
							  [gx[i+1,j],  gy[i+1,j]],
							  [gx[i,j],    gy[i,j]]])
				for i in range(gx.shape[0]-1) for j in range(gx.shape[1]-1)]

	g = np.zeros(2)
	for p in polygons:
		m2 = (p.intersection(mass_dist).area / p.area) * density
		rhat = np.array([p.centroid.x - m1.x, p.centroid.y - m1.y]) 
		rhat /= (rhat[0]**2 + rhat[1]**2)**0.5
		g += m1.mass * m2 / p.centroid.distance(geom.Point(m1.x, m1.y))**2 * rhat
	g *= G
	
	return g

theta = np.linspace(0, np.pi*2, 100)
r = np.cos(theta*2+np.pi)+5+np.sin(theta)+np.cos(theta*3+np.pi/6)
m = pointMass(5.0, 20.0, 0.0)
g = netForce(r, m)

plt.figure(figsize=(12, 6))
plt.axis('off')
plt.plot(np.cos(theta)*r, np.sin(theta)*r, color='k', lw=0.5, linestyle='-')
plt.scatter(m.x, m.y, s=20, color='k')
plt.text(m.x, m.y-1, r'$m$', ha='center')
plt.text(1, -1, r'$M$', ha='center')
ghat = g / (g[0]**2 + g[1]**2)**0.5
plt.quiver([m.x], [m.y], [ghat[0]], [ghat[1]], width=0.004, scale=0.25, scale_units='xy')
plt.text(m.x - 5, m.y + 1, r'$F = ({{{:.3g}}}, {{{:.3g}}})$'.format(g[0], g[1]))
plt.gca().set_aspect('equal')
plt.savefig('./GravitationalForceDiagram.2.png', bbox_inches='tight', dpi=300)
plt.show()
