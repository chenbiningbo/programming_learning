"""
    作者：陈笔
    版本：5.0
    时间：17/08/2019
    功能：利用爬虫抓取空气质量
"""
import requests

def get_html_text(url):
    r = requests.get(url,timeout=30)
    print(r.status_code)
    return r.text

def main():
    city_pinyin = input('请输入城市的拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''
    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()