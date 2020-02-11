"""
    作者：陈笔
    版本：4.0
    时间：06/08/2019
    功能：判断密码强度
         2.0 新增循环终端
         3.0 保存设置的密码到文件中
         4.0 读取保存的密码
"""

def check_number_exist(password_str):

    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break

    return  has_number

def check_letter_exist(password_str):

    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return  has_letter


def main():

    f = open('password_3.0.txt', 'r')
    for line in f.readlines():
        print('read:{}'.format(line))

    f.close()

if __name__ == '__main__':
    main()