"""
7. 判断 101~200 有多少个素数，并输出所有的质数

"""
list1 = []

for i in range(101, 201):
    list1.append(i)

print(list1)


list2 = []

for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            if j == i-1:
                print('这个是质数：', i)
                list2.append(i)
            else:
                continue


print('总数：', len(list2))
print('列表：', list2)
