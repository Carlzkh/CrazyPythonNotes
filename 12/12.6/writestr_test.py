import os

'''
os.linesep和\r\n的效果一样，换行后有个空行，等于换两行
\n只会换一行，没有空行
'''

f = open('x.txt', 'w+')
# os.linesep代表当前操作系统上的换行符
f.write('我爱Python' + os.linesep)
f.writelines(('土门壁甚坚，',
              '杏园度亦难。' + os.linesep,
              '势异邺城下，\r\n',
              '纵死时犹宽。\n'))
