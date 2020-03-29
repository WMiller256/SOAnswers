# Question: https://stackoverflow.com/questions/60905558/live-update-international-space-station-location-in-cartopy-map

import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import cartopy.crs as ccrs

url = 'http://api.open-notify.org/iss-now.json'

plt.figure(figsize=(10,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

s = plt.scatter([], [], color='blue', marker='o')

def animate(i):
	r = requests.get(url)
	data = r.json()

	dt = data['timestamp']
	lat = data['iss_position']['latitude']
	lon = data['iss_position']['longitude']

	s.set_offsets([float(lon), float(lat)])
	time.sleep(30)

anim = FuncAnimation(plt.gcf(), animate, frames = 20)
anim.save('./iss.gif', writer='imagemagick')
