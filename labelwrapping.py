import textwrap
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('miller')

df = {'Client Name': ['Some Name', 'Some long company name', 'Name',
 		    'Company', 'Long Comany Name'],
 	  'Col 1': [51235, 152, 12554, 12464, 12434]}
data = pd.DataFrame(df)

fig, ax = plt.subplots(1)

width = 7
ax.set_yticklabels([textwrap.fill(i, width) for i in data['Client Name'].head()])
plt.savefig("./LabelWrapping-wrapped.png", bbox_inches='tight', dpi=300)

ax.set_yticklabels(data['Client Name'].head())
plt.savefig("./LabelWrapping-unwrapped.png", bbox_inches='tight', dpi=300)
