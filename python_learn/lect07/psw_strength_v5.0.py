"""
    作者：陈笔
    版本：4.0
    时间：06/08/2019
    功能：判断密码强度
         2.0 新增循环终端
         3.0 保存设置的密码到文件中
         4.0 读取保存的密码
         5.0 将相关方法封装成一个整体，面向对象编程
"""

class PasswordTool:
    """
        密码类工具
    """
    def __init__(self,password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    # 类的方法
    def process_password(self):
        # 规则1：密码长度是否大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('你输入的密码小于8位！')

        # 规则2：要包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求含有数字！')

        # 规则3：要包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求含有字母')

    def check_number_exist(self):

        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return  has_number

    def check_letter_exist(self):

        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return  has_letter


def main():

    try_times = 5
    while try_times > 0:
        password = input('请输入你的密码:')

        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open('password_5.0.txt','a')
        f.write('密码：{},强度：{}\n'.format(password,password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格')
            try_times -= 1
        print()
    if try_times <= 0:
        print('尝试次数太多，密码设置失败！')
if __name__ == '__main__':
    main()