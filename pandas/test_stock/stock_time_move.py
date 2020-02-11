import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

stock_code = '0700.hk'
start_date = '2000-1-1'
end_date = pd.datetime.now()
stock_info = data.get_data_yahoo(stock_code, start_date, end_date)

fig, ax = plt.subplots(2, sharex=True)

tecent = stock_info['Close'].asfreq('D', method='ffill')
tecent.plot(ax=ax[0], color='r')
tecent.shift(365).plot(ax=ax[1], color='b')
plt.show()
