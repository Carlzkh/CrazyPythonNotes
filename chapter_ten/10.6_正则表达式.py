"""
写正则表达式的时候尤其需要注意空格
"""
import re

p = re.compile(r'1[358]\d{9}')
s = '1521525323652phone number:15215537653,hello1525156532656,13213562355,12535665232162,162515465677555'
l1 = p.search(s)  # 返回第一个符合正则的字符串的Match对象，
print(l1)
l1 = re.search(r'(?P<phoneno>1[358]\d{9})', s)  # 返回第一个符合正则的字符串的Match对象，
print(l1)
print(l1.groupdict())
l2 = p.match(s)  # 从字符串开始位置匹配正则，成功则返回Match对象
print(l2)
l2 = p.match(s).groups()  # 从字符串开始位置匹配正则，成功则返回Match对象
print(l2)
l2 = p.match(s).group()  # 从字符串开始位置匹配正则，成功则返回Match对象
print(l2)
l2 = p.match(s).group(0)  # 从字符串开始位置匹配正则，成功则返回Match对象
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

print('以p分隔字符串，返回列表，最后一个参数是分割次数：', re.split(p, 'q, 3w, 15215536524e, r', 1))  # 返回列表，max split表示最大分隔次数

# 在正则表达式中使用组
m = re.search(r'(kit).(org)', r"www.kit.org is a good domain")
print(m.group(0))  # kit.org
# 调用简化写法，底层是调用m.__getitem__(0)
print(m[0])  # kit.org
print(m.span(0))  # (4, 12)
print(m.group(1))  # kit
# 调用简化写法，底层是调用m.__getitem__(1)
print(m[1])  # kit
print(m.span(1))  # (4, 8)
print(m.group(2))  # org
# 调用简化写法，底层是调用m.__getitem__(2)
print(m[2])  # org
print(m.span(2))  # (9, 12)
# 返回所有组所匹配的字符串组成的元组
print(m.groups())
# 正则表达式定义了2个组，并为组指定了名字
m2 = re.search(r'(?P<prefix>kit).(?P<suffix>org)', r"www.kit.org is a good domain")
print(m2.groupdict())  # {'prefix': 'kit', 'suffix': 'org'}

print(re.search(r'Windows (95|98|NT|2000) [\w]+ \1', 'Windows 98 published 98'))  # 最后的\1代表第一个组匹配的字符串，不匹配返回None
print(re.search(r'Windows (95|98|NT|2000) [\w]+ \1', 'Windows 98 published 95'))  # 最后的\1代表第一个组匹配的字符串，不匹配返回None
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))

# print(re.search(r'Windows (?:95|98|NT|2000) [a-z ]+ \1', 'Windows 98 published in 98'))
print(re.search(r'Windows (?:95|98|NT|2000) [a-z ]+', 'Windows 98 published in 98'))
print(re.search(r'Windows (95|98|NT|2000) [a-z ]+', 'Windows 98 published in 98'))
yw = re.search(r'industr(?:y|ies)', 'industries')  # 没有组
ww = re.search(r'industr(y|ies)', 'industries')  # 有组
print(yw.group(0))  # yw.group(1)报错，因为yw没有组
print(ww.group(1))
print(re.search(r'industry|industries', 'industries'))

print(re.search(r'@.+\.', 'sun@fkit.com.cn'))  # 贪婪匹配，match='@fkit.com.'
print(re.search(r'@.+?\.', 'sun@fkit.com.cn'))  # 非贪婪匹配（勉强匹配），match='@fkit.'
