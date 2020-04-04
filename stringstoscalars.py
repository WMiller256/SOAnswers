import pandas as pd
from pandas import DataFrame
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df = pd.read_csv("data.csv")
pd.set_option("display.max_rows",None,"display.max_columns", None)

x = pd.to_datetime(df["Date"], format = "%m/%d/%Y")
fort = df["Fort McHenry Channel"].values
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=29))
plt.plot(x,fort)
plt.gcf().autofmt_xdate()
plt.legend(["fort", ])
plt.xlabel("Dates")
plt.ylabel("Matter")
plt.savefig("./out.png", bbox_inches='tight', dpi=400)
plt.show()
