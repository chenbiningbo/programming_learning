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

tencent = stock_info['Close'].asfreq('D', method='ffill')
rolling = tencent.rolling(365)
data = pd.DataFrame({'original': tencent, 'rolling-mean': rolling.mean(), 'rolling-std': rolling.std()})
data.plot(style=['-', '--', ':'])
plt.show()
