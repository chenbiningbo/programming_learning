"""
    作者：陈笔
    版本：1.0
    功能：模拟掷骰子
    日期：10/08/2019

"""

import random

# 定义掷骰子函数
def roll_dice():
    roll = random.randint(1,6)
    return roll


def main():

    #初始化参数
    total_times = 10000
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll == j:
                result_list[j - 1] += 1

    for i,result in enumerate(result_list,start=1):
        print('点数为{}的次数是：{}，频率：{}'.format(i,result,result / total_times))




if __name__ == '__main__':
    main()