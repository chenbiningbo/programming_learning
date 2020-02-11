'''
功能：计算年化波动率，年化波动率=日收益率波动差*（年交易量 **0.5）
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from math import sqrt

seaborn.set()


def get_data_ser(index_code, start_date, end_date, col_name):
    csv_name = 'csv/' + index_code + '.csv'
    df = pd.read_csv(csv_name, encoding='gbk')
    df = df.reindex(index=df.index[::-1])  # 顺序排列
    df.set_index('date', inplace=True)  # 将索引更换成日期
    date_index = pd.DatetimeIndex(df.index)
    ser = df.reindex(index=date_index)[col_name]

    select_time = pd.date_range(start_date, end_date)
    select_ser = ser[ser.index.isin(select_time)]
    return select_ser


def get_annual_ret_rate(index_code, begin_date, end_date):
    ser = get_data_ser(index_code, begin_date, end_date, 'close')
    total_trading_day = len(ser.index)
    annual_day_peryear = 244
    final_worth = ser.iloc[total_trading_day - 1]
    initial_worth = ser.iloc[0]
    annual_ret_rate = (pow((final_worth / initial_worth), (annual_day_peryear / total_trading_day)) - 1) * 100
    return annual_ret_rate


def get_volativity(index_code, begin_date, end_date):
    annual_day_peryear = 244
    ser = get_data_ser(index_code, begin_date, end_date, 'change')
    ser = pd.to_numeric(ser)
    ser = ser / 100
    volativity = ser.std() * sqrt(annual_day_peryear)
    return volativity


hs_300 = get_volativity('399300', '2004-1-1', '2020-1-1')
bond_index = get_volativity('000012', '2004-1-1', '2020-1-1')
print(hs_300)
print(bond_index)
