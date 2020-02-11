"""
    作者：陈笔
    版本：11.0
    时间：08/09/2019
    功能：用pychart插件
"""
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Style


# 主函数
def main():

    aqi_date = pd.read_csv('china_city_aqi.csv')

    # 数据清洗
    clean_aqi_data = aqi_date[aqi_date['AQI'] > 0]
    clean_aqi_data2 = clean_aqi_data[clean_aqi_data['AQI'] < 500]

    #排序 top 20
    top20_cites = clean_aqi_data2.sort_values(by=['AQI']).head(20)
    print('空气质量最好的城市：')
    print(top20_cites)

    # 绘图
    chart = Bar("全国空气质量最好的20个城市", Style.init_style)
    chart.add("aqi", top20_cites['city'], top20_cites['AQI'])
    page.add(chart)

if __name__ == '__main__':
    main()