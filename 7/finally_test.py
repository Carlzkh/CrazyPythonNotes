"""
除非在位 except 块中 调用了退出 Python 解释器的方法:os._exit(1)，否则不管在 try 块、
except 块中执行怎样的代码，出现怎样的情况，异常处理的 finally 块总会被执行
sys.exit()方法退出程序不能阻止 finally 块的执行，这是因为 sys.exit（）方法本身就是
通过引发 SystemExit 异常来退出程序的。
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
    finally:
        # fis.close()
        print('执行finally')


foo()
