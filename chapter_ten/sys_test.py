import sys
print([e for e in dir(sys) if not e.startswith('_')])
'''
 sys.argv 获取运行 Python 程序的命令行参数。其中 ys.argv[O ］通常就是指该 Python 程序，
sys.argv[ 代表为 Python 程序提供 个参数， sys.argv[2 ］代表为 Python 程序提供的第
个参数·…··依此类推。
~ sys .b yteorder ：显示本地宇节序的指示符。 如果本地字节序是大端模式， 该属性返回 big;
否则返回 little
~ sys .copyri ht 该属性返回与 Python 解释器有关的版权信息。
~ sys.executable 该属性返回 Python 解释器在磁盘上的存储路径。
~ sys.ex it （）：通过引发 Syste .Exit 异常来退出程序 将其放在 try 块中不能阻止 finally 块的
执行。
~ sys.flags: 亥只读属性返回运 Python 命令时指 的旗标
~ sys.getfilesystemencoding （）：返回在当前系统中保存文件所用的字符集。
~ sys.getr fcount object 返回指定对象的引用计数 前面介绍过 object 对象的引用计数
时，系统会回收该对象。

~ sys.getrecursionlimit（）：返回 Python 解释器当前支持的递归深度 该属性可通过
se ecursionlimit（）方法重新设置
~ sys .getswitch nterval （） 返回在当前 Python 解释器中线程切换的时间间隔。该属性可通过
setswitchinterval （）函数改变
>b sys. implement tion 返回当前 Pyt hon 解释器的实现
~ sys.maxsize ：返回 Python 整数支持的最大值。在 32 位平台上，该属性值为 2**31
64 位平台上，该属性值为 2**63 -
~ sys.modu es ：返回模块名和载入模块对应关系的字典
~ sys path ：该属性指定 Python 找模块的路径列表。 程序可通过修改该属性来动态增加
Python 加载模块的路径
~ sys .platform 返回 Python 解释器所在平台的标识符
sys tdin ：返回系统的标准输入流一一 个类文件对象
~ sys.stdout 返回系统的标准输出流一一 个类文件对象
sys tderr 返回系统的错误输出流一一 个类文件对象
> sys.version ：返回当前 Python 解释器的版本信息
};>- sys. winver ：返回当前 Python 解释器的主版本号
'''

# 显示本地字节序的指示符
print('sys.byteorder: ', sys.byteorder)
# 显示与 Python 解释器有关的版权信息
print('sys.copyright: ', sys.copyright)
# 显示 Python 解释器在磁盘上的存储路径
print('sys.executable: ', sys.executable)
# 显示在当前系统中保存文件所用的字符集
print('sys.get filesystemencoding: ', sys.getfilesystemencoding())
# 显示 Python 整数支持的最大值
print('sys.maxsize: ', sys.maxsize)
# 显示 Python 解释器所在的平台
print('sys.platform: ', sys.platform)
# 显示当前 Python 解释器的版本信息
print('sys.version: ', sys.version)
# 返回当前 Python 解释器的主版本号
print('sys.win ver: ', sys.winver)
