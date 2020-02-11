'''
目的：1、选择数据
     2、绘制图形

作者：陈笔
时间：2020年2月1日
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

def get_data_ser(index_code,start_date, end_date):
    csv_name = 'csv/' + index_code + '.csv'
    df = pd.read_csv(csv_name, encoding='gbk')
    df = df.reindex(index=df.index[::-1])  # 顺序排列
    df.set_index('date', inplace=True)     # 将索引更换成日期
    date_index = pd.DatetimeIndex(df.index)
    ser = df.reindex(index=date_index)['close']

    select_time = pd.date_range(start_date, end_date)
    select_ser = ser[ser.index.isin(select_time)]
    return select_ser

index_code = input('please input index code:')
begin_date = pd.to_datetime(input('input start date:'))
end_date = pd.to_datetime(input('input end date:'))
# HS_300_ser = get_data_ser('399300', '2019-1-1', '2020-1-1')
HS_300_ser = get_data_ser(index_code, begin_date, end_date)

# print(HS_300_ser)
HS_300_ser.plot()
plt.show()
