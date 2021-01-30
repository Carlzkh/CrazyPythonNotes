from sys import argv
# 输出 argv 列表的长度
print(len(argv))
# 遍历 argv 列表的每一个元素
for argv in argv:
    print(argv)

'''
执行过命令和结果
D:\\CrazyPythonNotes>python D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py
1
D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py

D:\\CrazyPythonNotes>python D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py Python Swift
3
D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py
Python
Swift

D:\\CrazyPythonNotes>python D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py "Python Swift"
2
D:\\CrazyPythonNotes\\chapter_ten\\argv_test.py
Python Swift

D:\\CrazyPythonNotes>

'''


'''
前面介绍了使用 PYTHON PATH 环境变量来添加Python模块的加载路径，但这种方式必须预先设置好。
如果需要在程序运行时动态改变Python模块的加载路径， 则可通过sys.path属性来实现
sys.path 是很有用的一个属性，它可用于在程序运行时为 Python 动态修改模块加载路径。例如下程序在运行时动态指定加载 g:\tk_ex 目录下的模块。

程序清单：
import sys 
＃动态添加 g:\\fk_ext 路径作为模块加载路径
sys.path.append ('g:\\fk_ext') 
＃加载 g:\\fk ext 各径下的 hello 模块
import hello 

为了成功运行该程序，需要在 g＼盘中创建 fk_ext 目录，并在该目录下添加 hello.py 模块文件
'''
