"""1. 提示用户输入一个N 表示用户接下来要输入N个字符串，程序尝试将用户输入的每一
字符串用空格分割成两个整数，并结算这两个整数整除的结果 。要求 使用异常处理机制来处理用
户输入的各种错误情况，并提示用户重新输入。
"""


class CarlException(Exception):
    pass


N = input('输入N个字符串：')
while N != 'exit':
    try:
        calculate = N.split(' ')
        # print(len(calculate))
        # print(calculate)
        if len(calculate) != 2:
            raise CarlException('自定义错误')
        number = int(calculate[0]) // int(calculate[1])
        print(number)
        N = input('输入N个字符串：')
    except Exception as e:
        print('输入错误，使用空格分隔两个数字', e)
        N = input('输入N个字符串：')


# 参考答案：
str_n = input('请输入整数N: ')
try:
    n = int(str_n)
    print(n)
    i = 0
    while True:
        try:
            a, b = input('请输入2个整数(空格隔开): ').split()
            print(int(a) // int(b))
            i += 1
            if i >= n: break
        except:
            print('务必输入空格隔开的2个整数!')
except:
    print('请输入整数N!')












