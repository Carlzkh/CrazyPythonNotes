"""
列表与元组的通用方法
元组不能修改
只要不涉及元素改变的情况，元组与列表的方法都是通用的
"""


'''
1、通过索引访问元素
可以使用中括号索引：0代表第一个，-1代表最后一个，包含前括号，不包含后括号
'''
list1 = [1, 2, 3, 4, 5]
print(list1[0])
print(list1[-1])

'''
2、子序列
切片，步长
步长不为负数
'''
print(list1[1:3])
print(list1[0:6:2])


'''
3、加法
列表只能加列表，不能加元组
元组只能加元组，不能加列表
结果：所有元素组成的新列表/元组
'''
list2 = [6, 7, 8, 9, 0]
print(list1 + list2)

'''
4、乘法
重复N次
'''
print(list1 * 2)

'''
5、in运算符
判断元素在不在
'''
print(1 in list1)
print(1 not in list1)
print(1 in list2)


'''
6、长度、最大、最小
python以此判断字符的Ascii码值，来判断字符串大小

'''
print(len(list1))
print(min(list1))
print(max(list1))


'''
7、序列封包、序列解包
sequence_packing:多个值赋给一个变量，自动封装成元组
sequence——unpacking：多个变量接受一个元组或列表，自动按顺序赋值给每个变量（变量数与元素个数要相同）
d, e, f = 4, 5, 6
多变量赋值，其实是先执行序列封包再执行序列解包
'''
tuple1 = 1, 2, 3
print(type(tuple1), tuple1, sep='\n')
a, b, c = tuple1
print(a, b, c)
d, e, f = 4, 5, 6
print(d, e, f)

