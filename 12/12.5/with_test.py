import codecs
import fileinput

# 使用with语句打开文件，该语句会负责关闭文件
with codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True) as f:
    for line in f:
        print(line, end='')


with open("readlines_test.py", 'r', 1, 'utf-8') as f:
    for line in f:
        print(line, end='')


# 使用with语句打开文件，该语句会负责关闭文件
with fileinput.input(files=('test.txt', 'info.txt')) as f:
    for line in f:
        print(line, end='')
