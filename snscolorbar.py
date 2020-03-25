import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.DataFrame({'Count' : [9729, 9567, 10576, 15789],
				   'loan_status' : [0.971323, 0.951814, 0.941944, 0.929761],
				   'sub_grade' : ['A1', 'A2', 'A3', 'A4']})

plt.figure(figsize = (12, 8))
g = sns.barplot(x="sub_grade", y = "Count", data=df, palette=cm.Blues(df['loan_status']))

plt.colorbar(cm.ScalarMappable(cmap=cm.Blues))
plt.savefig('./SNSColorbar.png', bbox_inches='tight', dpi=300)
plt.show()
