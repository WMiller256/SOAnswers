# Question: https://stackoverflow.com/questions/61239033/
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.dates import MonthLocator, DateFormatter

data = np.random.randint(0, 50, (10, 61))
dates = [datetime.strptime('01-01-2000', '%m-%d-%Y') + timedelta(d) for d 
         in range(len(data[0]))]
clevels = np.arange(0, 50, 5)

fig, ax = plt.subplots(figsize=(10, 5))
im  = ax.contourf(dates, range(data.shape[0]), data, levels=clevels, 
                      cmap='RdBu_r', extend='both')

ax.set_ylabel("Level")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter("%m/%d/%Y"))
cbar = plt.colorbar(im, values=clevels, pad=0.01)
plt.savefig('./monthlocator.png', bbox_inches='tight', dpi=400)
plt.show()
