"""
    作者：陈笔
    版本：2.0
    日期：05/08/2019
    功能：输入某年某月，判断这是第几天
         2.0增加功能 用列表来替换元组
"""

from datetime import datetime

def is_leap_year(year):

    is_leap = False

    if (year % 400 == 0) or ( (year %4 == 0)) and (year % 100 !=0):
        is_leap = True
    return is_leap

def main():
    input_date = datetime.strptime(input('请输入日期（yyyy/mm/dd）：'),'%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前月份天数的总和及当前月份的天数
    days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month - 1]) + day


    print('这是{}年的第{}天。'.format(year,days))
if __name__ == '__main__':
    main()