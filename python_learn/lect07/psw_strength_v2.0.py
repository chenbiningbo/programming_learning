"""
    作者：陈笔
    版本：2.0
    时间：06/08/2019
    功能：判断密码强度
         2.0 新增循环终端
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

    try_times = 5
    while try_times > 0:

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
        else:print('密码要求含有数字！')

        #规则3：要包含字母
        if check_letter_exist(password):
            strengh_level += 1
        else:print('密码要求含有字母')

        if strengh_level == 3:
            print('恭喜，密码强度合格')
            break
        else:
            print('密码强度不合格')
            try_times -= 1
        print()


    if try_times <=0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()