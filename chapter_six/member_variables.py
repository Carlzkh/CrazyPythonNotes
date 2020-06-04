"""
成员变量：

"""

'''
1、类变量和实例变量

'''


class Address:
    detail = '广州'
    post_code = '510660'

    def info(self):
        # 尝 式直接访问类变量
        # print(detail ）＃报错
        # 通过类来访问类变量
        self.detail = 3
        print(Address.detail)
        print(Address.post_code)
        # 通过类来访问 Address 类的类变量


print(Address.detail)  # 输出广1+1
address = Address()
address.info()
# 修改 Address 类的类变量
Address.detail = '佛山'
Address.post_code = '460110'

address.info()








































