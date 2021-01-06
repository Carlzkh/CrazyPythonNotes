"""
7. 用户输入以空格分隔的多个整数，程序将这些整数转换成元组元素，并输出该元组及其 Hash
值（使用内置的 hash 函数）。
"""
s = input("输入多个整数，以空格分隔：")
list1 = s.split(' ')
tuple1 = tuple(list1)
Hash = hash(tuple1)
print(tuple1, Hash)


