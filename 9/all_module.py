"""
如果使用“from 模块名 import ＊”这样的语句来导入模块，程序会导入该模块
中所有不以下画线开头的程序单元，这是很容易想到的结果。
有时候模块中虽然包含很多成员，但并不希望每个成员都被暴露出来供外界使用，此时可借助
于模块的 all 变量，将变量的值设置成 个列表，只有该列表中的程序单元才会被暴露出来
"""

# 测试＿all＿变量的模块

_a = 1
b = 2


def hello():
    print('Hello, Python')


def world():
    print('Python World is funny')


def test():
    print(' －－ test 一－')


# 定义＿all ＿变量，默认只导入 hello world 两个程序单元
__all__ = ['hello', 'world']
