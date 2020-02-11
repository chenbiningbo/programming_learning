'''
功能：对股票和债券的配置进行合理计算
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

def get_stock_with_bond(stock_code, stock_share, bond_code, bond_share, begin_date, end_date):
    stock_ser = get_data_ser(stock_code, begin_date, end_date, 'close')
    stock_ser = stock_ser / stock_ser.iloc[0]
    bond_ser = get_data_ser(bond_code, begin_date, end_date, 'close')
    bond_ser = bond_ser / bond_ser.iloc[0]

    comb_ser = pd.Series(index=stock_ser.index)

    stock_unit = stock_share
    bond_unit = bond_share

    for i in range(len(stock_ser.index)):
        comb_ser.iloc[i] = stock_unit*stock_ser[i] + bond_unit*bond_ser.iloc[i]
        if i % 244 == 0 and i!=0:
            stock_unit = (comb_ser.iloc[i]*stock_share) / stock_ser.iloc[i]
            bond_unit = (comb_ser.iloc[i]*bond_share) / bond_ser.iloc[i]

    return comb_ser

comb_ser55 = get_stock_with_bond('399300', 0.5, '000012', 0.5, '2004-5-13', '2019-5-13')
comb_ser82 = get_stock_with_bond('399300', 0.8, '000012', 0.2, '2004-5-13', '2019-5-13')
hs_300 = get_data_ser('399300', '2004-5-13', '2019-5-13', 'close')
hs_300 = hs_300 / hs_300.iloc[0]

bond_index = get_data_ser('000012', '2004-5-13', '2019-5-13', 'close')
bond_index = bond_index / bond_index.iloc[0]
df = pd.DataFrame({'hs-300':hs_300,
                   'bond-index':bond_index,
                   'comb55':comb_ser55,
                   'comb82':comb_ser82})


df.plot()
plt.show()

