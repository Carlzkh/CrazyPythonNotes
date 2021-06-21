"""

2利用第 题定义的 Student 类，定义 个列表保存 Student 对象作为通讯录数据 。程序
可通过 name email address 查询，如果找不到数据，则进行友好提示
"""
from one import Student

contacts = [Student('菩提', 5000, 'MALE', '02028309765',
                    '灵台方寸山三心斜月洞', 'pu@crazyit.org'),
            Student('孙悟空', 500, 'MALE', '02028309358',
                    '花果山水帘洞', 'sun@crazyit.org'),
            Student('牛魔王', 650, 'MALE', '02028309378',
                    '积雷山摩云洞', 'niu@crazyit.org'),
            Student('白骨精', 230, 'FEMALE', '13699881122',
                    '白骨岭', 'bai@crazyit.org'),
            Student('猪八戒', 500, 'MALE', '13588889999',
                    '福临山云栈洞', 'zhu@crazyit.org')]


def find_by_name(name):
    for x in contacts:
        if name == x.name:
            y = x
            break
        else:
            y = '不存在'
    return y


def find_by_email(email):
    return [x for x in contacts if email in x.email]


def find_by_address(address):
    return [x for x in contacts if address in x.address]


if __name__ == '__main__':
    t = input('请输入查找的方式, 名字(n), Email(e), 地址(a): ')
    k = input('请输入查找的关键字: ')
    if t == 'n':
        print(find_by_name(k))
    elif t == 'e':
        print(find_by_email(k))
    elif t == 'a':
        print(find_by_address(k))
    else:
        print('输入有误!')






