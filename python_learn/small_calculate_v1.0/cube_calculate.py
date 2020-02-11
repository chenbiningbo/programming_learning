"""
    作者：陈思诺
    版本：1.0
    日期：12/08/2019
    功能：计算正方体的各种数值
"""

length = int(input('请输入你要计算的正方体棱长(整数)：'))
# 计算油漆面的数量

one_side_num = 6 * (length - 2) ** 2
two_side_num = (length - 2) * 12
three_side_num = 8
none_num = (length - 2) ** 3


print('这个正方体分割后\n一面油漆的数量是：{}\n两面油漆的数量是：{}\n'
      '三面油漆的数量是：{}\n没有油漆的数量是：{}\n'
      .format(one_side_num,two_side_num,three_side_num,none_num))