"""
2. 给定 list ，将该列表的从 start 到 end 的所有元素复制到另一个 list
"""
list1 = []
N = int(input("输入个数N："))
for i in range(N):
    element = input("输入%d个元素，第%d个" % (N, (i+1)))
    list1.append(element)

list2 = []
for i in range(N):
    list2.append(list1[i])

print(list2)
print(id(list2))
print(list1)
print(id(list1))
# list3 = list1
# print(list3)
# print(id(list3))
