"""
所有的异常对象都包含了如下几个常用属性和方法
~ args ：该属性返回异常的错误编号和描述字符串
~ errno ：该属性返回异常的错误编号。
~ strerror ：该属性返回异常的描述宇符串。
~ with_traceback（）： 通过该方法可处理异常的传播轨迹信息。
"""


def foo():
    try:
        fis = open('a.txt')
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)


foo()






