"""
7. 提示用户输入两行，第 1行是所有学习 Python 的学员编号（以逗号隔开），第 2行是所有
学习 Java 的学员编号（以逗号隔开），计算既学 Python 又学 Java 的学员的数量。
"""
string1 = input('输入两行,第1行是所有学习python的学员编号(以逗号隔开)')
string2 = input('输入第二行,第2行是所有学习Java的学员编号(以逗号隔开)')
list_python = string1.split(',')
list_java = string2.split(',')
list_java_and_python = []
for i in list_python:
    if i in list_java:
        list_java_and_python.append(i)

print(len(list_java_and_python))
print(list_java_and_python)
