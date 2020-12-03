import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

plt.style.use('./miller.mplstyle')

plt.figure(figsize=(12,3))
x = np.arange('2020-04-03T00:00Z', '2020-04-05T00:30Z', np.random.randint(50, 70), dtype='datetime64[m]')
x = np.delete(x, np.s_[4:10])
x = np.delete(x, np.s_[25:32])
y = np.sin(np.linspace(0, np.pi*2, len(x))*2 + np.random.random(len(x)) - 0.5)
plt.plot(x, y)

dx = np.arange(x[0], x[-1]+60, 60, dtype='datetime64[m]').astype(dt.datetime)
fill = [False if dt.time(8, 0, 0) < t.time() < dt.time(20, 0, 0) else True for t in dx]
plt.tick_params(axis='x', rotation=90)
plt.fill_between(dx, plt.ylim()[0], plt.ylim()[1], where=fill, fc='grey', alpha=0.2)
plt.subplots_adjust(bottom=0.3)
plt.savefig('./conditionalshading.png', bbox_inches='tight', dpi=400)
plt.show()
