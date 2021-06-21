"""
2. 提示用户输入一个整数，如果用户输入的整数是奇数，则输出“有趣”；如果用户输入的整
数是偶数，且在 2~5 之间，则打印“没意思”；如果用户输入的整数是偶数，且在 6-20 之间，则
输出“有趣”；如果输入的整数是其他偶数，则打印“没意思”。要求 ：使用异常处理机制来处理用
户输入的各种错误情况
"""
N = int(input('输入整数：'))
while N != 'exit':
    try:
        if N % 2 == 1:
            print('有趣')
            N = int(input('输入整数：'))
        elif 2 < N < 5:
            print('没意思')
            N = int(input('输入整数：'))
        elif 6 < N < 20:
            print('有趣')
            N = int(input('输入整数：'))
        else:
            print('没意思')
            N = int(input('输入整数：'))
    except Exception as e:
        print('请输入整数！')
        N = int(input('输入整数：'))


# 参考答案
while True:
    str_n = input('请输入整数N: ')
    if str_n == 'exit':
        import sys
        sys.exit(0)
    try:
        n = int(str_n)
        if n % 2 != 0:
            print('有趣')
        elif 5 > n > 2:
            print('没意思')
        elif 20 > n > 6:
            print('有趣')
        else:
            print('没意思')
    except:
        print('务必输入整数')


