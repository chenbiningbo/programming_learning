"""
    作者：陈笔
    版本：3.0
    功能：模拟掷骰子
    日期：10/08/2019
    2.0功能：模拟掷两个骰子
    3.0功能：可视化投掷两个骰子结果

"""

import random
import matplotlib.pyplot as plt

# 定义掷骰子函数
def roll_dice():
    roll = random.randint(1,6)
    return roll

# 主函数
def main():

    #初始化参数
    total_times = 100                             # 初始化掷骰子的次数
    result_list = [0] * 11                          # 初始化存储列表
    roll_list = list(range(2,13))                   # 初始化点数
    roll_dict = dict(zip(roll_list,result_list))    # 将以上两个数列打包
    roll1_list = []
    roll2_list = []

    for i in range(total_times):                    #
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2,13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for i,result in roll_dict.items():
        print('点数为{}的次数是：{}，频率：{}'.format(i,result,result / total_times))


    # 数据可视化输出
    x = range(1,total_times + 1)
    plt.scatter(x,roll1_list,c='red',alpha=0.5)
    plt.scatter(x,roll2_list,c='green',alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()