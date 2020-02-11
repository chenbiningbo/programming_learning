import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

stock_code = '0700.hk'
start_date = '2019-4-4'
end_date = '2019-5-4'
stock_info = data.get_data_yahoo(stock_code, start_date, end_date)
fig, ax = plt.subplots(2, sharex=True)
# print(stock_info.head())
# print(stock_info['Close'].asfreq('D'))


stock_info['Close'].asfreq('D').plot(ax=ax[0], marker='o')
stock_info['Close'].asfreq('D', method='bfill').plot(ax=ax[1], color='b', style='--', alpha=0.5)
stock_info['Close'].asfreq('D', method='ffill').plot(ax=ax[1], color='r', alpha=0.5)
plt.legend(['back-fill', 'front-fill'], loc='upper left')
plt.show()
# stock_info.to_csv('../tecent_20190404_20190504.csv')