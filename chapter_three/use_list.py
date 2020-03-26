"""
列表可以增删改查
元组数据更安全
"""
'''
1、创建列表
直接赋值
list()函数
'''
list1 = [1, 2, 3, 4, 5]
list2 = list((6, 7, 8, 9, 0))
print(list1, list2, sep='\n')


'''
2、增加列表元素
append()将元组或列表作为一个整体直接加到列表中作为一个元素
extend(),不可以增加单个元素；将元组或列表中的元素加到列表中
'''
list1.append(1)
list2.append(list1)
print(list1, list2, sep='\n')

# list1.extend(1)
list2.extend(list1)
print(list1, list2, sep='\n')


'''
3、删除列表元素
del语句
remove()函数:删除找到的第一个值，没找到会报错
clear()函数：清除所有值

'''
del list2[0]
print(list2)
del list2[1:2]
print(list2)
del list2[0:8:2]
print(list2)
list2.remove(9)
print(list2)









































