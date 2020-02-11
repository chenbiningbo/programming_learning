'''
功能：年化收益率=（最终价值/初始价值）** 244/总交易日 -1

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()


def get_data_ser(index_code, start_date, end_date):
    csv_name = 'csv/' + index_code + '.csv'
    df = pd.read_csv(csv_name, encoding='gbk')
    df = df.reindex(index=df.index[::-1])  # 顺序排列
    df.set_index('date', inplace=True)  # 将索引更换成日期
    date_index = pd.DatetimeIndex(df.index)
    ser = df.reindex(index=date_index)['close']

    select_time = pd.date_range(start_date, end_date)
    select_ser = ser[ser.index.isin(select_time)]
    return select_ser


def get_annual_ret_rate(index_code, begin_date, end_date):
    ser = get_data_ser(index_code, begin_date, end_date)
    total_trading_day = len(ser.index)
    annual_day_peryear = 244
    final_worth = ser.iloc[total_trading_day - 1]
    initial_worth = ser.iloc[0]
    annual_ret_rate = (pow((final_worth / initial_worth), (annual_day_peryear / total_trading_day)) - 1) * 100
    return annual_ret_rate


print('hs-300:')
print('3 years:{}'.format(round(get_annual_ret_rate('399300', '2017-1-1', '2020-1-1'), 2)) + '%')
print('5 years:{}'.format(round(get_annual_ret_rate('399300', '2015-1-1', '2020-1-1'), 2)) + '%')
print('8 years:{}'.format(round(get_annual_ret_rate('399300', '2012-1-1', '2020-1-1'), 2)) + '%')
print('10 years:{}'.format(round(get_annual_ret_rate('399300', '2010-1-1', '2020-1-1'), 2)) + '%')
print('15 years:{}'.format(round(get_annual_ret_rate('399300', '2005-1-1', '2020-1-1'), 2)) + '%')

print('bound-index:')
print('3 years:{}'.format(round(get_annual_ret_rate('000012', '2017-1-1', '2020-1-1'), 2)) + '%')
print('5 years:{}'.format(round(get_annual_ret_rate('000012', '2015-1-1', '2020-1-1'), 2)) + '%')
print('8 years:{}'.format(round(get_annual_ret_rate('000012', '2012-1-1', '2020-1-1'), 2)) + '%')
print('10 years:{}'.format(round(get_annual_ret_rate('000012', '2010-1-1', '2020-1-1'), 2)) + '%')
print('15 years:{}'.format(round(get_annual_ret_rate('000012', '2005-1-1', '2020-1-1'), 2)) + '%')

HS_300 = get_data_ser('399300', '2005-1-1', '2020-1-1')
HS_300 = HS_300 / HS_300.iloc[0]
BOND_index = get_data_ser('000012', '2005-1-1', '2020-1-1')
BOND_index = BOND_index / BOND_index.iloc[0]

df = pd.DataFrame({'HS-300':HS_300,
                   'BOND-index':BOND_index})
df.plot()
plt.show()