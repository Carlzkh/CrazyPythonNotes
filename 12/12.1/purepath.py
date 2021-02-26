from pathlib import *

# 创建PurePath，实际上使用PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))  # <class 'pathlib.PureWindowsPath'>
pp = PurePath('crazyit', 'some/path', 'info')
# 看到输出Windows风格的路径
print(pp)  # 'crazyit\some\path\info'
pp = PurePath(Path('crazyit'), Path('info'))
# 看到输出Windows风格的路径
print(pp)  # 'crazyit\info'
# 明确指定创建PurePosixPath
pp = PurePosixPath('crazyit', 'some/path', 'info')
# 看到输出Unix风格的路径
print(pp)  # crazyit/some/path/info


# 如果不传入参数，默认使用当前路径
pp = PurePath()
print(pp)  # .

# 如果传入参数包含多个根路径，则只有最后一个根路径及后面子路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)  # /usr/lib64
pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp)  # d:info

# 在Windows风格路径中，只有盘符才算根路径
pp = PureWindowsPath('c:/Windows', '/Program Files')
print(pp)  # c:\Program Files

# 路径字符串中多出来的斜杠和点号（代表当前路径）都会被忽略
pp = PurePath('crazyit//info')
print(pp)  # crazyit\info
pp = PurePath('crazyit/./info')
print(pp)  # crazyit\info
pp = PurePath('crazyit/../info')
print('crazyit/../info', pp)  # crazyit\..\info，相当于找和crazyit同一级的info路径


# 比较两个Unix风格的路径，区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO'))  # False
# 比较两个Windows风格的路径，不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO'))  # True
# Windows风格的路径不区分大小写
print(PureWindowsPath('INFO') in {PureWindowsPath('info')})  # True
# Unix风格的路径区分大小写,所以'D:'小于'c:'
print(PurePosixPath('D:') < PurePosixPath('c:'))  # True
# Windows风格的路径不区分大小写,所以'd:'（D:）大于'c:'
print(PureWindowsPath('D:') > PureWindowsPath('c:'))  # True


# 不同风格的路径可以判断是否相等（总不相等）
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))  # False
# 不同风格的路径不能判断大小，否则会引发异常
# print(PureWindowsPath('info') < PurePosixPath('info')) # TypeError

pp = PureWindowsPath('abc')
# 将多个路径拼起来（Windows风格的路径）
print(pp / 'xyz' / 'wawa')  # abc\xyz\wawa
pp = PurePosixPath('abc')
# 将多个路径拼起来（Unix风格的路径）
print(pp / 'xyz' / 'wawa')  # abc/xyz/wawa
pp2 = PurePosixPath('haha', 'hehe')
# 将pp、pp2两个路径连接起来
print(pp / pp2)  # abc/haha/hehe

pp = PureWindowsPath('abc', 'xyz', 'wawa')
print(str(pp))  # abc\xyz\wawa
pp = PurePosixPath('abc', 'xyz', 'wawa')
print(str(pp))  # abc/xyz/wawa

# 访问drive属性
print(PureWindowsPath('c:/Program Files/').drive)  # c:
print(PureWindowsPath('/Program Files/').drive)  # ''
print(PurePosixPath('/etc').drive)  # ''

# 访问root属性
print(PureWindowsPath('c:/Program Files/').root)  # \
print(PureWindowsPath('c:Program Files/').root)  # ''
print(PurePosixPath('/etc').root)  # /

# 访问anchor属性
print(PureWindowsPath('c:/Program Files/').anchor)  # c:\
print(PureWindowsPath('c:Program Files/').anchor)  # c:
print(PurePosixPath('/etc').anchor)  # /

# 访问parents属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])  # abc\xyz\wawa
print(pp.parents[1])  # abc\xyz
print(pp.parents[2])  # abc
print(pp.parents[3])  # .
# 访问parent属性
print(pp.parent)  # abc\xyz\wawa

# 访问name属性
print(pp.name)  # haha
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)  # bb.txt

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问suffixes属性
print(pp.suffixes[0])  # .txt
print(pp.suffixes[1])  # .tar
print(pp.suffixes[2])  # .zip
# 访问suffix属性
print(pp.suffix)  # .zip
print(pp.stem)  # bb.txt.tar

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)  # abc\xyz\wawa\haha
# 转成Unix风格的路径
print(pp.as_posix())  # abc/xyz/wawa/haha
# 将相对路径转换成Uri引发异常
# print(pp.as_uri()) # ValueError
# 创建绝对路径
pp = PurePath('d:/', 'Python', 'Python3.6')
# 将绝对路径转换成Uri
print(pp.as_uri())  # file:///d:/Python/Python3.6

# 判断当前路径是否匹配指定模式
print(PurePath('a/b.py').match('*.py'))  # True
print(PurePath('/a/b/c.py').match('b/*.py'))  # True
print(PurePath('/a/b/c.py').match('a/*.py'))  # False

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试relative_to方法
print(pp.relative_to('c:/'))  # abc\xyz\wawa
print(pp.relative_to('c:/abc'))  # xyz\wawa
print(pp.relative_to('c:/abc/xyz'))  # wawa

# 测试with_name方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py'))  # e:\Downloads\fkit.py
# print(PureWindowsPath('c:/').with_name('fkit.py'))  # ValueError
# print(p.with_name('fkit.py'))  # ValueError

# 测试with_suffix方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))  # e:\Downloads\pathlib.tar.zip
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))  # README.txt
