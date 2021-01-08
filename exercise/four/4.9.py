"""
9. 输入一行字符， 分别统计出其中英文字母 、空格、数字和其他字符的个数
s.isalnum() 所有字符都是数字或者字bai母，du为真返回 Ture，否则zhi返回 False。（重点，这是字dao母数字一起判zhuan断的！！）
s.isalpha() 所有字符都是字母，为真返回 Ture，否则返回 False。（只判断字母）
s.isdigit() 所有字符都是数字，为真返回 Ture，否则返回 False。（只判断数字）
s.islower() 所有字符都是小写，为真返回 Ture，否则返回 False。
s.isupper() 所有字符都是大写，为真返回 Ture，否则返回 False。
s.istitle() 所有单词都是首字母大写，为真返回 Ture，否则返回 False。
s.isspace() 所有字符都是空白字符，为真返回 Ture，否则返回 False。
"""
s = input('输入一串字符串：')
english = 0
space = 0
number = 0
other = 0
for i in range(len(s)):
    if s[i].isalpha():
        print('这个是英文字母：', s[i])
        english += 1
    elif s[i].isdigit():
        print('这个数字：', s[i])
        number += 1
    elif s[i].isspace():
        print('这个是空格：', s[i])
        space += 1
    else:
        print('这个是其他字符：', s[i])
        other += 1

print('英文字母：', english, '数字：', number, '空格：', space, '其他：', other,sep='个\n')


