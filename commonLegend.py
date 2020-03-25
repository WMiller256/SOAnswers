import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df = pd.DataFrame(np.random.randint(0,100,size=(16,15)), columns=list('ABCDEFGHIJKLMNO'))
clr=["#1b0031","#3fee42","#b609d2","#c9ff5d","#7449f6","#03fca1","#9164ff","#ffaf06",
	 "#087dff","#ff5c0d","#0081b0","#fff276","#530069","#8cff9c","#ff56d7"]

df1=df.loc[0:3]
df1.loc[4]=clr
df1=df1.drop(columns=["A","M","J","F"])
clr1=list(df1.loc[4])
df1=df1.drop(4)

df2=df.loc[4:7]
df2=df2.reset_index(drop=True)
df2.loc[4]=clr
df2=df2.drop(columns=["B","M","K","L"])
clr2=list(df2.loc[4])
df2=df2.drop(4)

df3=df.loc[8:11]
df3=df3.reset_index(drop=True)
df3.loc[4]=clr
df3=df3.drop(columns=["D","L","F"])
clr3=list(df3.loc[4])
df3=df3.drop(4)

df4=df.loc[12:16]
df4=df4.reset_index(drop=True)
df4.loc[4]=clr
df4=df4.drop(columns=["G","I","N","O"])
clr4=list(df4.loc[4])
df4=df4.drop(4)

fig, axes = plt.subplots(nrows=2, ncols=2,sharex=True,figsize=(15,8))

df1.plot.area(ax=axes[0][0],color=clr1, legend=False)
df2.plot.area(ax=axes[1][0],color=clr2, legend=False)
df3.plot.area(ax=axes[0][1],color=clr3, legend=False)
df4.plot.area(ax=axes[1][1],color=clr4, legend=False)

handles = [Patch(color = clr[i], label = df.columns.values[i]) for i in range(len(clr))]
plt.figlegend(handles=handles)
plt.savefig('./CommonLegend.png', bbox_inches='tight', dpi=300)
plt.show()
