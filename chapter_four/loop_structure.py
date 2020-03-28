"""
循环：初始化、条件判断、循环体、迭代语句

"""
'''
1、while
'''
count_i = 1
while count_i < 5:
    print(count_i)
    count_i += 1
print("条件不满足，循环结束")

'''
2、循环遍历列表、元组
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_a = []
list_b = []
list_c = []
count_i1 = 0
while count_i1 < len(list1):
    if list1[count_i1] % 3 == 0:
        list_a.append(list1[count_i1])
    elif list1[count_i1] % 3 == 1:
        list_b.append(list1[count_i1])
    else:
        list_c.append(list1[count_i1])
    count_i1 += 1
print("能被3整除的数：", list_a)
print("除3余1的数：", list_b)
print("除3余2的数：", list_c)


'''
3、for-in循环
isinstance():判断变量是否是指定的类型
'''
factorial = int(input('输入想要计算的阶乘：'))
result = 1
list2 = []
for i in range(1, factorial + 1):
    list2.append(str(i))
    list2.append('*')
    print(str(i) + '*' + str(result))
    result = i * result
list2.pop()
# del list2[-1]
list2.append('= ')
print(list2)
print(' '.join(list2) + str(result))
# print(result)

'''
4、循环遍历字典
items()
keys()
values()

'''

'''
5、循环使用else
其实没啥用
'''

'''
6、嵌套循环
'''

'''
7、for表达式，返回列表
又叫列表推导式

'''
a_list = [x * x for x in range(10)]
print(a_list)

b_list = [x * x for x in range(10) if x % 2 == 0]
print(b_list)


'''
8、常用工具函数
zip(),压缩多个列表返回zip对象（可迭代对象，元素是元组）
reversed(),反序的迭代器
sorted(),传入可迭代对象，返回排序的列表，不改变传参的值

'''






















