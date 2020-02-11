"""
    作者：陈笔
    版本：9.0
    时间：08/09/2019
    功能：数据分析
"""
import pandas as pd



# 主函数
def main():

    aqi_date = pd.read_csv('china_city_aqi.csv')

    #基本统计
    print('AQI的最大值：', aqi_date['AQI'].max())
    print('AQI的最小值：', aqi_date['AQI'].min())
    print('AQI的均值：', aqi_date['AQI'].mean())

    #排序 top 10
    top10_cites = aqi_date.sort_values(by=['AQI']).head(10)
    print('空气质量最好的城市：')
    print(top10_cites)

    #排序 bottom 10
    bottom10_cites = aqi_date.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的城市：')
    print(bottom10_cites)

    #保存文件
    top10_cites.to_csv('top10_aqi.csv',index=False)
    bottom10_cites.to_csv('bottom10_aqi.csv',index=False)


if __name__ == '__main__':
    main()