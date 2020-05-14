import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb

forc=np.float_()
r=fits.open("/mnt/c/Users/words/Downloads/673nmos/673nmos.fits")[0].data
g=fits.open("/mnt/c/Users/words/Downloads/656nmos/656nmos.fits")[0].data
b=fits.open("/mnt/c/Users/words/Downloads/502nmos/502nmos.fits")[0].data

r = np.array(r,forc)*5
g = np.array(g,forc)*0.75
b = np.array(b,forc)*8

t = 250
r[r > t] = t
g[g > t] = t
b[b > t] = t

rgb_default = make_lupton_rgb(r,g,b,Q=0.001,stretch=300,filename="pillar.png")
plt.figure(figsize=(8,8))
plt.imshow(rgb_default, origin='lower')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig("./PillarsOfCreation.png", dpi=150)
plt.show()
