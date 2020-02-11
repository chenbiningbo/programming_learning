"""
    作者：陈笔
    功能：52周存钱挑战
    版本：5.0
    日期：04/08/2019
    增加功能：2.0记录每周的存款数
             3.0进行循环计数
             4.0灵活进行设置
             5.0根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
"""

import math
import datetime

# 计算n周内的存款金额
def save_money_in_n_weeks(money_per_week,increase_money,total_week):

    money_list = []  # 记录每周存款数
    saved_money_list = []

    for i in range(total_week):
        # 存钱操作

        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下周存钱金额
        money_per_week += increase_money

    return saved_money_list

def main():

    money_per_week = float(input('请输入每周存入的金额：'))         # 每周存入的金额
    increase_money = float(input('请输入每周递增金额：'))           # 递增的金额
    total_week = int(input('请输入总共周数：'))                      # 总共周数

    saved_money_list = save_money_in_n_weeks(money_per_week,increase_money,total_week)

    input_data_str = input('请输入日期（yyyy/mm/dd）:')
    input_date = datetime.datetime.strptime(input_data_str,'%Y/%m/%d')

    week_num = input_date.isocalendar()[1]
    print('第{}周的存款是:{}元'.format(week_num,saved_money_list[week_num - 1]))

if __name__ =='__main__':
    main()


input('press enter to exit...')