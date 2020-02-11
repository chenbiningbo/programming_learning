"""
    作者：陈笔
    功能：52周存钱挑战
    版本：2.0
    日期：04/08/2019
    增加功能：记录每周的存款数
"""

import math

def main():
    money_per_week = 10         # 每周存入的金额
    i = 1                       # 记录周数
    increase_money = 10         # 递增的金额
    total_week = 52             # 总共周数
    saving = 0                  # 账户累计
    money_list = []             # 记录每周存款数

    while i <= total_week:
        # 存钱操作
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i,money_per_week,saving))


        # 更新下周存钱金额
        money_per_week += increase_money
        i += 1
        print('本周存钱{}，累计存钱{}'.format(money_list, saving))
if __name__ =='__main__':
    main()