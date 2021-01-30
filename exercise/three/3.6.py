"""
6. 用户输入 N个字符扇，将这些字符串收集到列表中，然后去除其中重复的宇符串后输出列表
"""
import random
N = int(input("输入整数N："))
list1 = []
for i in range(N):
    list1.append(random.randint(0, 10))
print(list1)

# list1.sort()
j = 0
for i in range(len(list1)):

    if list1.count(list1[j]) > 1:
        for k in range(len(list1)):
            if k < len(list1) and list1[k] == list1[j]:
                del list1[j]
    elif j + 1 < len(list1):
        j = j + 1
    else:
        break


print(list1)
