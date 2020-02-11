"""
    作者：陈笔
    版本：4.0
    功能：模拟掷骰子
    日期：10/08/2019
    2.0功能：模拟掷两个骰子
    3.0功能：可视化投掷两个骰子结果
    4.0功能：直方图可视化
"""

import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义掷骰子函数
def roll_dice():
    roll = random.randint(1,6)
    return roll

# 主函数
def main():

    #初始化参数
    total_times = 100000                             # 初始化掷骰子的次数
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    # 数据可视化输出
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()