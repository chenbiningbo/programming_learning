"""
    作者：陈笔
    版本：5.0
    日期：05/08/2019
    功能：输入某年某月，判断这是第几天
         2.0增加功能 用列表来替换元组
         3.0增加功能，用集合来代替
         5.0 增加功能，用一行代码来解决问题
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

    # # 包含30天的月份集合
    # _30_days_month_set = {4,6,9,11}
    # _31_days_month_set = {1,3,5,7,8,10,12}

    mon_day_dict = {1:31,
                    2:28,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31}

    # 初始值
    days = 0
    days += day

    for i in range(1,month):
        days += mon_day_dict[i]


    if is_leap_year(year) and month > 2:
        days += 1


    print('这是{}年的第{}天。'.format(year,days))
if __name__ == '__main__':
    main()