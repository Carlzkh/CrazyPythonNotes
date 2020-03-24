"""
深入使用字符串

"""

'''
1、转义字符
\b      退格
\t      制表符
\n      换行
\r      回车
\'      单引号
\"      双引号
\\      反斜杠

'''
print('aa\b制表符\t换行\n回 车\r啊\'\"\\')

'''
2、格式化字符串输出：默认右对齐，不够位数左边补空格
%s,字符串
%d，整型
%f，浮点型
%后面加数字，可以限定字符串最小宽度
-：指定左对齐
+：数值总要带着符号
0：表示不补空格，补0

浮点型，还可以指定小数位数
字符串也可以指定最大位数，称为精度值
'''

userName = 'Carl'
userAge = 18
print('姓名：%s，年龄：%d' % (userName, userAge))

print('年龄10位:%10d' % userAge)
print('指定左对齐：%-d' % userAge)
print('数值带着符号：%+d' % userAge)
print('最短10位，不够补0：%010d' % userAge)
Π = 3.141592654
print('最大八位，保留两位小数：%8.2f' % Π)
print('最大八位，保留两位小数，左边补零：%08.2f' % Π)
print('最大八位，保留两位：%8.2s' % userName)
print('最大八位，左对齐，保留两位：%-8.2s' % userName)

'''
3、序列相关方法
可以使用中括号索引：0代表第一个，-1代表最后一个，包含前括号，不包含后括号
len()函数获取长度
min()函数获取最小字符
max()
in操作符判断包含
'''
str1 = 'Carl is a good man'
print(str1[0])
print(str1[0:])
print(str1[-1])
print(str1[:-1])
print(str1[1:3])
print(len(str1))
print(min(str1))
print(max(str1))
print('Carl' in str1)
print('Carlz' in str1)


'''
4、大小写相关方法
dir()：列出指定类或模块的所有内容，方法、函数、变量等
help()：给出指定函数的帮助文档
title():每个首字母大写
lower():每个字母小写
upper():每个字母大写
'''
print(str1.title())
print(str1.lower())
print(str1.upper())


'''
5、删除空白：
strip()删除字符串前后的空白
lstrip()删除字符串前面（左边）的空白
rstrip()删除字符串后面（右边）的空白
这三个方法不改变字符串本身
这三个方法可以传参字符串，删除参数中有的在字符串前后连续的字符
'''
str2 = '  Carl is a good man  '
print(str2.strip())
print(str2.lstrip())
print(str2.rstrip())
str2 = 'Carl is a good man'
print(str2.strip('Crlmn'))
print(str2.lstrip('Crlmn'))
print(str2.rstrip('Crlmn'))


'''
6、查找、替换
startswith():判断字符串是否以子串开头
endswith():判断字符串是否以子串结尾
find():寻找子串在字符串中的位置，没有子串返回-1
index():寻找子串在字符串中的位置，没有子串报错
replace():使用指定子串代替字符串中的目标子串
translate():使用指定映射对字符串执行替换
maketrans():创建翻译映射表

'''


'''
7、连接、分割
split():按指定字符分割
join():
'''

str3 = '  Carl is a good man  '
print(str3.split())
print(str3.split(None, 2))
list1 = str3.split()
print('_'.join(list1))



























