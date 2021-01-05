"""
7. 通过学习我们知道str是不可变的，本程序要实现一个功能：用户输入一个字符串，修改该
字符串中哪个位置的字符，程序就会输出修改后的结果。比如用户输入
'fkjava.org'
6 -
程序将会输出： fkjava-org
"""
s = input('输入字符串：')
i = int(input('修改位置：'))
r = input('代替字符：')
new = s.replace(s[i], r, 1)
print(new)

