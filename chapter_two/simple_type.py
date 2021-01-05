"""
一、数值类型：
1、整型     int
2、浮点型   float
3、复数     complex
二、字符串：
string
"""

'''
整型，包括None
四种进制表示：
十进制：100
二进制：0b1100100或0B1100100
八进制：0o144或0O144, # 后面是大小写的字母欧
十六进制：0x64或0X64

'''
a = 100
b = 0b1100100
c = 0o144
d = 0x64
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
'''
浮点型
浮点型必须包含小数点
只有浮点型才可以使用科学计数法，如：512E2是浮点数51200.0而不是整型51200


'''
evaluate = 5e3
print(type(evaluate))

'''
复数
虚数部分用j或J来表示
形式如下，a,b为实数
compx = a + bj

'''

