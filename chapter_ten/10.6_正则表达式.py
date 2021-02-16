import re

p = re.compile(r'1[358]\d{9}')
s = '1521525323652phone number:15215537653,hello1525156532656,13213562355,12535665232162,162515465677555'
l1 = p.search(s)  # 返回第一个符合正则的字符串的Match对象，
print(l1)
l2 = p.match(s)  # 从字符串开始位置匹配正则，成功则返回Match对象
print(l2)
l3 = p.findall(s)  # 返回所有符合正则的子串的列表
print(l3)
l4 = p.finditer(s)  # 返回所有符合正则的子串的迭代器
print(l4)
print(l4.__next__())
print(l4.__next__())
print(l4.__next__())
print(l4.__next__())
print(l4.__next__())
# print(l4.__next__())  # 超出下标
print(p.sub('zkh', s))  # 参数顺序千万不能写反了！！！！！
print(re.sub(p, 'zkh', s))  # 返回全部替换后的字符串
print(re.sub(p, 'zkh', s, 2))  # 返回2次替换后的字符串（只替换前面两处符合正则的子串）

s1 = '15215537653'
print(re.fullmatch(r'\d{11}', s1))  # 全匹配，则返回Match对象，否则返回None

print(re.split(p, 'q, 3w, 15215536524e, r', 1))  # 返回列表，max split表示最大分隔次数













