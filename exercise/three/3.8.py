"""
8.用户随机输入 N个大写字母，程序使用 dict 统计用户输入的每个字母的次数
"""
s = input("随机输入N个大写字母：")

dict1 = {s[0]: s.count(s[0])}

j = 1
for i in range(len(s)):
    if j + 1 <= len(s) and s[j] != s[i]:
        dict1[s[j]] = s.count(s[j])
        j += 1


print(dict1)






