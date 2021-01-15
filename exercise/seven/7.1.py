"""
1. 提示用户输入 一个N表示用户接下来要输入N个宇符串，程序尝试将用户输入的每一个
字符串 用空格分割成两个整数，并结算 这两个整数整除的结果 。要求 使用异常处理机制来处理用
户输入的各种错误情况，并提示用户重新输入。
"""
try:
    n = int(input('输入一个整数N：'))
    for i in range(n):
        str1 = input('输入一个字符串：')
        x, y = str1.split(' ')
        result = int(x) // int(y)
        print(result)
except (WindowsError, Exception) as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    # 访问异常的错误编号
    # print(e.errno)
    # 访问异常的详细信息
    # print(e.strerror)

'''
exception异常类没有errno和strerror属性
WindowsError异常类没有ZeroDivisionError异常
'''