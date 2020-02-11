"""
    作者：陈笔
    版本：4.0
    时间：17/08/2019
    功能：json保存成CSV
"""
import json
import csv
import os

# 解码json文件
def process_json_file(filepath):

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):

    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        city_list = csv.reader(f)
        for row in city_list:
            print(', '.join(row))

def main():

    filepath = input('请输入json文件名称：')

    file_name, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        process_json_file(filepath)
    if file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('这是一个支持的而文件格式！')

if __name__ == '__main__':
    main()