from matplotlib import pyplot as plt
import matplotlib.dates as mdate
import pandas as pd 
import numpy as np
import datetime
from decimal import Decimal
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data =[(datetime.date(2019, 12, 23), Decimal('0.3230'), Decimal('157.89')),
		(datetime.date(2019, 12, 23), Decimal('0.1680'), Decimal('157.74')),  
		(datetime.date(2019, 12, 23), Decimal('0.1440'), Decimal('152.78')),  
		(datetime.date(2019, 12, 24), Decimal('0.1070'), Decimal('157.94')),  
		(datetime.date(2019, 12, 24), Decimal('0.6420'), Decimal('159.81')),   
		(datetime.date(2019, 12, 25), Decimal('0.0980'), Decimal('115.31')),   
		(datetime.date(2019, 12, 26), Decimal('0.0830'), Decimal('122.89')),    
		(datetime.date(2019, 12, 26), Decimal('0.1600'), Decimal('171.88')),   
		(datetime.date(2019, 12, 27), Decimal('0.1710'), Decimal('161.40')),   
		(datetime.date(2019, 12, 30), Decimal('0.0590'), Decimal('161.02')),   
		(datetime.date(2019, 12, 30), Decimal('0.4150'), Decimal('168.19')),   
		(datetime.date(2019, 12, 31), Decimal('0.1150'), Decimal('167.83')),   
		(datetime.date(2020, 1, 2), Decimal('0.0790'), Decimal('192.41')),   
		(datetime.date(2020, 1, 3), Decimal('0.4930'), Decimal('216.43')),   
		(datetime.date(2020, 1, 3), Decimal('0.2640'), Decimal('154.92')),   
		(datetime.date(2020, 1, 3), Decimal('0.1980'), Decimal('211.11')),   
		(datetime.date(2020, 1, 10), Decimal('0.2173'), Decimal('248.64')),   
		(datetime.date(2020, 1, 13), Decimal('1.3202'), Decimal('196.34')),   
		(datetime.date(2020, 1, 14), Decimal('0.0423'), Decimal('198.30')),   
		(datetime.date(2020, 1, 16), Decimal('0.0236'), Decimal('296.56')),   
		(datetime.date(2020, 1, 16), Decimal('0.0937'), Decimal('304.03'))]

df = pd.DataFrame(data)
df.rename(columns={0:'a',1:'b',2:'c'},inplace=True)
x = df.a
y = df.c
fig,ax=plt.subplots(figsize=(10,5))
ax.scatter(x,y,facecolor='g',alpha=0.5)
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
_x = x.drop_duplicates()
ax.set_xticks(_x)
td = datetime.timedelta(days=2)
ax.set_xlim([min(_x)-td, max(_x)+td])
fig.autofmt_xdate()
plt.savefig('./PandasDateRange.2.png', bbox_inches='tight', dpi=300)
plt.show()
