"""
字符串入门
"""
'''
引号的处理，转义
两个单引号包含双引号或两个双引号包含单引号
\用反斜杠转义
'''
str1 = '"we are scared, Let\'s hide in the shade ", says the bird.'
print(str1)

'''
拼接字符串
1、两个字符串写一起，会自动拼接
2、用+号
'''
str2 = 'hello,'" Carl!"
print(str2)
str3 = ' Welcome to earth'
str4 = str2 + str3
print(str4)

'''
repr()与str()
均可以把数值变成字符串，repr会返回字符串python表达式：带引号的
'''
str5 = "This book's price is: "
num1 = 100
# print(str5 + num1) 会报错TypeError: can only concatenate str (not "int") to str
print(str5 + repr(num1))
print(str5 + str(num1))
print(repr(str5))  # repr函数会将带引号的该字符串返回
print(str(str5))

'''
python2中的raw_input()等同于python3中的input()
input()函数总是返回字符串，使用该值赋予变量的时候一定要记住它是字符串格式
'''
print(input('请输入：'))


'''
长字符串：用三引号括起来，可以包含任何字符
一行的字符串或表达式太长，需要换行，要使用\进行转义
'''

num2 = 3 * 4 + 4 / 2 \
    + 2
print(num2)

str6 = 'hello carl,\
welcome to earth'
print(str6)

str7 = '''"Let's go fishing",said Mary.
"OK, Let's go",said her brother
They walked to a lake
'''
print(str7)

str8 = """"Let's go fishing",said Mary.
"OK, Let's go",said her brother
They walked to a lake
"""
print(str8)


'''
原始字符串
r''
以r开头，会把反斜杠当成字符串的一部分，不会当成转义字符，
但是原始字符串仍然需要对引号进行转义
因此原始字符串结尾不能是反斜杠（他会转义最后的引号），要么分开，要么不用原始字符串
'''
str9 = r'\t\n\\g'
print(str9)
str10 = r'"Let\'s go"'
print(str10)

'''
字节串
'''
