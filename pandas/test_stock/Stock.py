'''
功能：利用pandas_datareader 从yahoo获取股票数据。
      示例的是从yahoo获取腾讯（0700.hk）的历史数据

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from pandas_datareader import data

seaborn.set()

stock_code = '0700.hk'
start_date = '2000-1-1'
end_date = '2019-10-1'
stock_info = data.get_data_yahoo(stock_code, start_date, end_date)

# print(stock_info.head(10))
#
# plt.plot(stock_info['Close'], 'b')
# # plt.savefig('tecent.png')
# plt.show()

stock_info['Close'].plot(color='b', alpha=0.5, style='-')
stock_info['Close'].resample('BA').mean().plot(color='r', alpha=0.5, style=':')
stock_info['Close'].asfreq('BA').plot(color='g', alpha=0.5,style='--')

plt.legend(['original', 'resample', 'asfreq'], loc='upper left')
plt.show()



# stock_info1 = data.get_data_yahoo('600795.ss', '1995-1-1', pd.datetime.now())
# print(stock_info1.head(10))
# stock_info1.to_csv('../test_stock/out.csv')
#
# plt.plot(stock_info1['Close'], 'r')
# # plt.savefig('tecent.png')
# plt.show()
