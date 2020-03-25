from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from scipy.stats import norm

np.random.seed(8)

def get_xs(lwr_bound = -4, upr_bound = 4, n = 80):
    return np.arange(lwr_bound, upr_bound, (upr_bound - lwr_bound) / n)
    
def get_distribution_params(list_):
    mus = [round((i + 1) + 0.1 * np.random.randint(0,10), 3) for i in range(len(dists))]
    sigmas = [round((i + 1) * .01 * np.random.randint(0,10), 3) for i in range(len(dists))]
    return mus, sigmas

def get_distributions(list_, xs, mus, sigmas):
    return [list(zip(xs, norm.pdf(xs, loc=mus[i], scale=sigmas[i] if sigmas[i] != 0.0 else 0.1))) 
            for i in range(len(list_))]

dists = [1, 2, 3, 4]
xs = get_xs()
mus, sigmas = get_distribution_params(dists)
distributions = get_distributions(dists, xs, mus, sigmas)

fc = [mcolors.to_rgba('r', alpha=0.6), mcolors.to_rgba('g', alpha=0.6), 
      mcolors.to_rgba('b', alpha=0.6), mcolors.to_rgba('y', alpha=0.6)]

poly = PolyCollection(distributions, fc=fc)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.add_collection3d(poly, zs=np.array(dists).astype(float), zdir='z')
ax.view_init(azim=115)
ax.set_zlim([0, 5])
ax.set_ylim([0, 5])
ax.set_xlim([0, 5])
plt.show()
