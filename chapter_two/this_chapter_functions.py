"""
本章函数总结，使用方法，参数含义
"""

# 输出函数print
'''
print(*values,sep=str,end:str,file:sys.stdout,flush:flase)
values:输出的值，可以有多个，可以是常量也可以是变量
sep：控制输入各个值之间的分割符，默认是空格
end：控制输出行尾的字符，默认是换行“/n”
file：控制输出至某个特定的文件，默认打印在屏幕上sys.stdout
flush：输出缓存，一般设置成flase就好

'''
name = 'Carl'
age = 18
print('姓名:', name, '年龄:', age, sep='\t', end='$')












