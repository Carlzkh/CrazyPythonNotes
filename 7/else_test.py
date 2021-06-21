"""
放在 else 块中的代码所引发 异常不会被 except 块捕获。
果希望某段代码的异常能被后面 except 块捕款，那么就应该 这段代码放在 try 块的代
码之后 如果希望某段 异常能向外传播（不被 except 块捕获〉，那么就应该将这段代码放在
else 块中。
"""


def else_test():
    s = input('请输入除数：')
    result = 20 / int(s)
    print('20 除以%s的结果是：%g' % (s, result))


def right_main():
    try:
        print('try 块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        # 将 else_test 放在 else 块中
        else_test()


def wrong_main():
    try:
        print('try 块的代码 没有异常')
        # 将 else test 放在 try 块的代码的后面
        else_test()
    except:
        print('程序出现异常')


wrong_main()
right_main()