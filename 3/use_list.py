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

'''
4、修改列表元素
对元素赋值：
对切片赋值：不限制变量个数与切片内元素数量一致，不一致时增加或删除元素
对切片赋值不能使用单个值
对切片赋值，带步长：限制变量个数与切片内元素数量一致
'''
print('*******************')
print(list2)
list2[1] = 3
print(list2)
list2[1:4] = '3'
print(list2)
list2[1:2] = 3, 4, 5
print(list2)
list2[0][0:6:2] = 3, 4, 5
print(list2)

'''
5、其他方法
count():计数
index():查询元素下标，没查到会报错，可以指定开始结束位置
pop():删除最后一个元素，可以实现出栈功能（先入后出）
reverse():元素反序
sort():排序,key=len,按元素长度排序，reverse=True，反序
'''
list3 = [1, 2, 3, 3, 'hello', 'h', 'a']
print(list3.count(3))
print(list3.count('h'))
print(list3.index(3))
print(list3.pop())
print(list3)
print(list3.reverse())
print(list3)
list4 = [3, 4, 2, 4, 2, 4, 1, 5]
print(list4.sort())
print(list4)
print(list4.sort(reverse=True))
print(list4)
#print(list3.sort(key=len, reverse=True)),数值没有len
#print(list3)


















