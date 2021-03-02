"""
txt另存为，选择ASNI编码就可以输出中文！！！！！，不会乱码
"""
import fileinput
# 一次读取多个文件
for line in fileinput.input(files=('info.txt', 'test.txt')):
    # 输出文件名，当前行在当前文件中的行号
    print(fileinput.filename(), fileinput.filelineno(), line, end='')
# 关闭文件流
fileinput.close()
