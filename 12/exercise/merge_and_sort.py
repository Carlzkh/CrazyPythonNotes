"""
1. 有两个磁盘文件 text1.txt text2.txt ，各存放一行英文字母，要求把这两个文件中的信息合
并（按字母顺序排列），然后输出到 个新文件 text3.txt
"""
with open('text1.txt') as f1:
    text1 = f1.read()
with open('text2.txt') as f2:
    text2 = f2.read()
rvt = (list(text1) + list(text2))
print(rvt)
rvt.sort()
print(rvt)
print(''.join(rvt))
print(type(str(rvt)))
with open('text3.txt', 'w+') as f3:
    f3.write("".join(rvt))
    # f3.write(str(rvt)),行不通
