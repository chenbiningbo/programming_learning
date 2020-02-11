"""
    作者：陈笔
    版本：10.0
    时间：08/09/2019
    功能：数据清洗再数据分析
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 主函数
def main():

    aqi_date = pd.read_csv('china_city_aqi.csv')

    # 数据清洗，只保留AQI大于0的数据
    # filter_condition = aqi_date['AQI'] > 0
    # clean_aqi_data = aqi_date[filter_condition]
    clean_aqi_data = aqi_date[aqi_date['AQI'] > 0]
    clean_aqi_data2 = clean_aqi_data[clean_aqi_data['AQI'] < 500]

    #基本统计
    print('AQI的最大值：', clean_aqi_data2['AQI'].max())
    print('AQI的最小值：', clean_aqi_data2['AQI'].min())
    print('AQI的均值：', clean_aqi_data2['AQI'].mean())

    #排序 top 20
    top20_cites = clean_aqi_data2.sort_values(by=['AQI']).head(20)
    print('空气质量最好的城市：')
    print(top20_cites)

    #排序 bottom 20
    bottom20_cites = clean_aqi_data2.sort_values(by=['AQI'], ascending=False).head(20)
    print('空气质量最差的城市：')
    print(bottom20_cites)

    # 绘图
    # top20_cites.plot(kind='bar', x='city', y='AQI', title='质量最好的20个城市',
    #                  figsize=(10,5))
    top20_cites.plot(kind='bar', x='city', y='AQI', title='质量最好的20个城市',
                     figsize=(10,5))
    plt.savefig('top20_aqi_hist.png')
    plt.show()
    #保存文件
    top20_cites.to_csv('top20_aqi.csv',index=False)
    bottom20_cites.to_csv('bottom20_aqi.csv',index=False)


if __name__ == '__main__':
    main()