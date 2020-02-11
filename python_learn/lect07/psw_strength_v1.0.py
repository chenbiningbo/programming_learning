"""
    作者：陈笔
    版本：1.0
    时间：06/08/2019
    功能：判断密码强度
"""

def check_number_exist(password_str):

    for c in password_str:
        if c.isnumeric():
            return  True
    return  False

def check_letter_exist(password_str):

    for c in password_str:
        if c.is():
            return  True
    return  False


def main():

    password = input('请输入你的密码:')

    # 密码强度
    strengh_level = 0

    # 规则1：密码长度是否大于8
    if len(password) >= 8:
        strengh_level += 1
    else:
        print('你输入的密码小于8位！')

    # 规则2：要包含数字
    if check_number_exist(password):
        strengh_level += 1
    else:print('密码要求含有')

    #规则3：要包含字母
    if check_letter_exist(password):
        strengh_level += 1



if __name__ == '__main__':
    main()