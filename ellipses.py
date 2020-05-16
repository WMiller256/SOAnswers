import shapely.geometry as geom
from shapely import affinity
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('miller')

n = 360
theta = np.linspace(0, np.pi*2, n)

a = 2
b = 1
angle = 45.0

r = a * b  / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)
xy = np.stack([r * np.cos(theta), r * np.sin(theta)], 1)

ellipse = affinity.rotate(geom.Polygon(xy), angle, 'center')

x, y = ellipse.exterior.xy
plt.plot(x, y, lw = 1, color='k')
ng = 50
rnd = np.array([[ii, jj] for ii in np.linspace(min(x),max(x),ng) for jj in np.linspace(min(y),max(y),ng)])

res = np.array([p for p in rnd if ellipse.contains(geom.Point(p))])

plt.scatter(rnd[:,0], rnd[:,1], s = 50, color=tableau20[1])
plt.scatter(res[:,0], res[:,1], color=tableau20[0], s = 15)
plt.savefig('./EllipseContains.png', bbox_inches='tight', dpi=300)
plt.show()
