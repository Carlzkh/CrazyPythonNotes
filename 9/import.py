"""
import A as a
from A import B as b

import 此 模块名[as别名1］，模块名2[as别名2]： 导入整 模块
from 模块名 import 成员名[as别名1］，成员名2[as别名2] ，… 导入模块中指定成员
上面两种 import 语句的区别主要有:
>第一种 import 语句导入整个模块内的所有成员（包括变量 函数、类等）；
第二种 import语句只导入模块内的指定成员（除非使用 form 模块名 import ＊，但通常不推荐使用这种语法）。
>当使用第一种 import 句导入模块中 的成 时，必须添加模块名或模块别名前缀
当使用第二种import 语句导入模块中的成员时，无须使用任何前缀，直接使用成员名或成员别名即可。

右击当前文件夹，选择 mark_directory_as---->Sources Root，可以解决自定义模块导入时，文件名下红色波浪线提示的问题
因为报错的根本原因是：究其根本是这些路径没有一个依据，也就是没有一个参照路径，它不知道哪个是根路径，所以在导入时找不到现有路径


使用“ import fk module ”导入模块的本质就是 fk modul .py 中的全部代码加载到内存井
执行，然后 整个模块 容赋值给与模块同名 变量，该变量 类型是 module ，而在该模块中定
义的所有程序单元都相当于该 dule 对象的成员
用“from fk_module import name, hello 导入模块中成员的本质就是：将 fk module.py
全部代码加载到内存并执行，然后只导入指定变量、函数等成员单元，并不会将整个模块导入，因
此上面程序在输出 fk modul 时将看到错误提示 'fk module’ is not defined o

"""
import sys
print(sys.argv)

# 导入 sys OS 两个模块,并为sys指定别名s, 为OS指定别名o。
import sys as s, os as o
# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)

from sys import argv
# 使用导入成员的语法 直接使用成员名访问
print(argv[0])

from sys import argv as v
print(v[0])

from sys import argv, winver
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
print(winver)

from sys import argv as v, winver as wv
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
print(wv)

import module1
print(module1.__doc__)

import module1 as md
# import module1 as md 两次导入只会生效一次
print(md.my_book)
md.say_hi('Charlie')
user = md.User('孙悟空')
print(user)
user.walk()
