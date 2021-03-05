"""
w+、wb+模式打开文件，会先清空文件，无论写入什么，文件都是最新的
a+、ab+模式打开文件，则不会清空，会在文件末尾追加
"""
import os
f = open('z.txt', 'a+')
# os.linesep代表当前操作系统上的换行符
f.write('我爱Python' + os.linesep)
f.writelines(('土门壁甚坚，' + os.linesep,
              '杏园度亦难。' + os.linesep,
              '势异邺城下，' + os.linesep,
              '纵死时犹宽。' + os.linesep))
