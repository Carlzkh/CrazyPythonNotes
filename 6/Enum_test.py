"""
枚举类
"""

import enum
# 定义 Season 枚举类
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))

# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season .SPRING.name)
# 访问枚举成员的值
print(Season .SPRING.value)

# 根据枚举变量名访问枚举对象
print(Season['SUMMER'])  # Season.SUMMER
# 根据枚举值访问枚举对象
print(Season(3))  # Season.FALL
'''此外， Python 还为枚举提供了 __members__ 属性，该属性返回一个 diet 字典 字典包含了
该枚举的所有枚举实例。程序可通过遍历 111 members 属性来访问枚举的所有实例。例如如下代码
（程序清单向上）。'''
# 遍历 Season 枚举的所有成员
for name, member in Season.__members__.items():
    print(name, '=>',  member, ',', member.value)
