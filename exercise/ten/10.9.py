"""
9. 提示用户输入 1个字符串，程序要输出该字符串中出现次数最多的 3个字符，以及对应的
出现次数。
"""
string1 = input('输入一个字符串：')
dict1 = {}
for i in string1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1


list_values = list(dict1.values())
list_values.sort()
print(list_values[-3:])
print(dict1)
print(list(dict1.keys())[list(dict1.values()).index(3)])
for i in range(1, 4):
    print(list(dict1.keys())[list(dict1.values()).index(list_values[-i])] + ': ' + str(list_values[-i]))




