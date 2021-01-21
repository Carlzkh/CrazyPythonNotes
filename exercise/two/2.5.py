"""
5. 用户输入一个字符串和一个子串，程序必须打印出给定子串在目标字符串中出现的次数
字符串遍历将从左到右进行，而不是从右到左 例如给定ABCDCDC’和’ CDC' ，程序输出2
"""
s = input('用户输入字符串：')
sub_s = input('用户输入字符串的子串：')
j = len(sub_s)
k = 0
for i in range(len(s)):
    if s[i:i + j] == sub_s:
        k = k + 1
print(k)
