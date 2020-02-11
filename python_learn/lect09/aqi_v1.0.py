"""
    作者：陈笔
    版本：1.0
    时间：11/08/2019
    功能：AQI空气质量指数计算
"""

# 范围缩放
def cal_linear(iaqi_lo,iaqi_hi,bp_lo,bp_hi,val):
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi

# 计算PM2.5的IAQI
def cal_pm_iaqi(pm_val):

    if 0 <= pm_val < 36:
        iaqi = cal_linear(0,50,0,35,pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50,100,0,pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(50,100,0,pm_val)
    else:
        pass


# 计算CO的IAQI
def cal_co_iaqi(co_val):
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        pass

def cal_aqi(param_list):

    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi

def main():

    print('请输入一下信息，用空格分开')
    input_str = input('(1)PM2.5,(2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])


    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    aqi_val = cal_aqi(param_list)
    print('空气质量指数为：{}'.format(aqi_val))

if __name__ == '__main__':
    main()