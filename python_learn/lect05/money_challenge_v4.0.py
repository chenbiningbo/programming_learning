"""
    作者：陈笔
    功能：52周存钱挑战
    版本：4.0
    日期：04/08/2019
    增加功能：2.0记录每周的存款数
             3.0进行循环计数
             4.0灵活进行设置
"""

import math

# 计算n周内的存款金额
def save_money_in_n_weeks(money_per_week,increase_money,total_week):

    saving = 0  # 账户累计
    money_list = []  # 记录每周存款数

    for i in range(total_week):
        # 存钱操作

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下周存钱金额
        money_per_week += increase_money
    return saving

def main():

    money_per_week = float(input('请输入每周存入的金额：'))         # 每周存入的金额
    increase_money = float(input('请输入每周递增金额：'))           # 递增的金额
    total_week = int(input('请输入总共周数：'))                      # 总共周数

    save_money_in_n_weeks(money_per_week,increase_money,total_week)
    print('总的存款金额：',saving)

if __name__ =='__main__':
    main()