"""
6. 户输入自己的成绩，程序会自动判断该成绩的类型 成绩>=90分用 A 表示，80~ 89 分用B表示，70~79 分用C 表示，其他的用 D表示

"""
s = int(input('输入成绩：'))
if s >= 90:
    print('A')
elif 80 <= s <= 89:
    print('B')
elif 70 <= s <= 79:
    print('C')
else:
    print('D')
