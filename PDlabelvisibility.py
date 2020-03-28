import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

foo = pd.DataFrame(np.random.randn(5, 5), columns='a b c d e'.split())

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
foo.plot.scatter(x='a', y='b', ax=ax1, c='c')
foo.plot.scatter(x='a', y='c', ax=ax2, c='c')
ax2.set_xlabel('xxx')
ax2.xaxis.get_label().set_visible(True)
plt.savefig('./PDLabelVisibility.png', bbox_inches='tight', dpi=400)
plt.show()
