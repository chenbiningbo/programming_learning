'''
目的：1、对所有的数据从原来的倒序排列修改成按照时间内顺序排列
     2、现在的索引是系统自动产生的，拟将索引调整成时间
     3、现在的时间是字符串调整成时间格式，以方便后的计算

作者：陈笔
时间：2020年2月1日
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

def get_data_ser(index_code):
    csv_name = 'csv/' + index_code + '.csv'
    df = pd.read_csv(csv_name, encoding='gbk')
    df = df.reindex(index=df.index[::-1])  # 顺序排列
    df.set_index('date', inplace=True)     # 将索引更换成日期
    date_index = pd.DatetimeIndex(df.index)
    ser = df.reindex(index=date_index)['close']

    return ser

HS_300_ser = get_data_ser('399300')
print(HS_300_ser)
HS_300_ser.plot()
plt.show()
