"""
    作者：陈笔
    版本：6.0
    功能：模拟掷骰子
    日期：10/08/2019
    2.0功能：模拟掷两个骰子
    3.0功能：可视化投掷两个骰子结果
    4.0功能：直方图可视化
    5.0功能：利用NumPy
    6.0功能：三个骰子
"""

import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



# 主函数
def main():

    #初始化参数
    total_times = 100000                             # 初始化掷骰子的次数

    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr + roll3_arr

    hist, bins = np.histogram(result_arr, bins=range(3,20))
    print(hist)
    print(bins)

    # 数据可视化输出

    plt.hist(result_arr, bins=range(3, 20), density=1, edgecolor='black', linewidth=1, rwidth=0.6)

    # 显示点数设置
    tick_lables = ['3点', '4点', '5点','6点',
                   '7点', '8点', '9点', '10点',
                   '11点', '12点', '13点', '14点',
                   '15点', '16点', '17点', '18点']
    tick_pos = np.arange(3, 19) + 0.5
    plt.xticks(tick_pos, tick_lables)

    plt.title('骰子点数统计')
    plt.xlabel('点数'),
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()