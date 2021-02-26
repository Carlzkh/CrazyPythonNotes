from pathlib import *

# 获取当前目录
p = Path('.')
# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上一级目录
p = Path('../')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/*.py'):
    print(x)
pp = PurePath()
print(pp)
# 获取g:/publish/codes对应的目录
p = Path('C:/Users/kunhe.zhang/PycharmProjects/CrazyPythonNotes/12/12.1')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/path.py'):
    print(x)


p = Path('a_test.txt')
# 以GBK字符集输出文本内容
result = p.write_text('''有一个美丽的新世界
它在远方等我
那里有天真的孩子
还有姑娘的酒窝''',  encoding='GBK')
# 返回输出的字符数
print(result)

# 指定以GBK字符集读取文本内容
content = p.read_text(encoding='GBK')
# 输出读取的文本内容
print(content)

# 读取字节内容
bb = p.read_bytes()
print(bb)
