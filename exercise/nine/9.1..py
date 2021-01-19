"""
1. 定义一个 geometry 模块，在该模块下定义 print_triangle(n）和 print_diamond(n）两个函数，分
别用于在控制台用星号打印 角形和菱形，并为模块和函数都提供文档说明
"""
import geometry  # Mark Directory as Sources Root 可以去除自定义模块下的红色波浪线！

geometry.print_triangle(3)
geometry.print_diamond(5)
print(geometry.__doc__)
print(geometry.print_triangle.__doc__)
print(geometry.print_diamond.__doc__)

