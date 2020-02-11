import pandas as pd
import numpy as np

# test1
# data1 = pd.to_datetime('2019-5-21')
# print(data1)
# print(data1.strftime('%Y-%m-%d, %a'))


# test2
# print(pd.to_timedelta(np.arange(12), unit='d'))
# data = pd.to_datetime('2019-5-21')
# print(data + pd.to_timedelta(np.arange(12), unit='D'))


# test3
# index = pd.DatetimeIndex(['2015-5-1', '2015-6-1',
#                           '2016-5-1', '2016-6-1',
#                           '2017-5-1', '2017-6-1'])
# data = pd.Series([3, 4, 5, 6, 7, 8], index)
# print(data)
#
# print(data['2015-5-1'])
# print(data['2015'])

# test4
dates1 = pd.date_range(start='2019-9-1', end='2019-9-15')
dates2 = pd.date_range(start='2019-11-1', end='2019-11-2', freq='h')

print(dates1)
print(dates2)