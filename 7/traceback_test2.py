"""
print_exc([limit[, file ］］）的 完整形式是 print_exception(etype, value, tb[, limit[, file ］］）， 在完整形
式中，前面 个参数用于分别指定异常的如下信息。
type： 指定异常类型
value ：指定异常值。
tb ：指定异常的 traceback 信息。
当程序处于 except 块中时 ，该 except 块所捕获的异常信息可通过 sys 对象来获取，其中
sys.exc_type sys.exc _value sys.exc_traceback 就代表当前 except 块内的异常类型、异常值和异常传播轨迹
简单来说 print_exc([limit[, file ］］）相当于如下形式
print_exception(sys.exc_etype , sys.exc_value , sys.exc_tb[, limit[, file ］］
也就是说，使用 print_exc([limit[, file］］）会自动处理当前 except 块所捕获的异常。该方法还涉及
两个参数
limit ：用于限制显示异常传播的层数，比如函数 A调用函数 B函数 B发生了异常，如果
指定 limit=1，则只显示函数 A里面发生的异常 如果不设置 limit 参数 ，则默认全部显示。
file ：指定将异常传播轨迹信息输出到指定文件中。如果不指定该参数，则默认输出到控制台。
借助于 traceback 模块的帮助，我们可以使用 except 块捕获异常，并在其中打印异常传播信息，
包括把它输出到文件中 例如如下程序。
"""


# 导入 traceback 模块
import traceback


class SelfException(Exception):
    pass


def main():
    first_method()


def first_method():
    second_method()


def second_method():
    third_method()


def third_method():
    raise SelfException('自定义异常信息')


try:
    main()
except:
    # 捕获异常，并将异常传播信息输出到控制台
    traceback.print_exc()
    # 捕获异常，并将异常传播信息输出到指定文件中
    traceback.print_exc(file=open('log txt', 'a'))
