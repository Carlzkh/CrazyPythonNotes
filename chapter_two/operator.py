"""
运算符：
1、赋值运算符：=，赋值表达式本身也是有值的，就是被赋的值，因此可以连续赋值
2、算术运算符：+ 加 - 减 * 乘 / 除  // 整除 % 取余（可以是整数也可以是小数） ** 乘方
3、位运算符：
4、索引运算符
5、比较运算符
6、逻辑运算符
7、三目运算符
8、in运算符

"""
'''
1、赋值运算符
赋值表达式本身也是有值的，就是被赋的值，因此可以连续赋值
'''
a = b = 20
print(a, b)

'''
2、算术运算符
+ 加 - 减 * 乘 / 除  // 整除 % 取余（可以是整数也可以是小数） ** 乘方
加号还可以连接字符串，减号可以当负号

'''
print(1//2)
print(4//2)
print(4//3)
print(4.0//2)
print(5 % 3)
print(5.2 % 3.1)
print(5.2 % -2.9)
print(5 ** 3)
print(4 ** 0.5)


'''
3、位运算符
& : 按位与，都为1时为1，其余为0
| : 按位或，都为0时为0，其余为1
^ : 按位异或，相同为0，不同为1
~ : 按位取反，0为1，1为0
<< : 左移，左移N位，右边补零（乘以2的N次方）
>> : 右移，右移N位，左边补符号位（正数补0，负数补1）（除以2的N次方）
正数：原码、反码、补码均一样
负数：原码符号位不变，按位取反得反码，反码加1得补码

'''


'''
索引运算符：[]


'''

a = 'abcdefghijklmn'
print(a[2:8:2])
print(a[0:8:2])
print(a[0:8:3])


'''
比较运算符
< , <= , > , >= , == , != , is not , is
== 只比较两个变量的值， is 要求变量引用一样的对象
'''


'''
逻辑运算符
and
or
not
'''

'''
三目运算符
True_statement if expression else False_statement
'''
a = input('a')
b = input('b')
print('a>b') if a > b else print('a<=b')

'''
in
not in 
判断子串在字符串内，子序列在序列内

'''
b = 'abcdefghijklmn'
print('abcd' in b)
print('abcd' not in b)



