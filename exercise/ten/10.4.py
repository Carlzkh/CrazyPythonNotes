"""
4. 提示用户输入 1个字符串，程序使用正则表达式获取该字符串中第一次重复出现的英文字
包括大小写〉。
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
"""
import re
strings = input('输入字符串：')
for i in strings:
    if i.isalpha():
        list1 = re.findall(i, strings, flags=re.I)
        if len(list1) > 1:
            print('重复字母的第一次出现：', i)
            print('第一次出现重复的时候（前面已经存在一次，这是第二次出现）：', list1[1])
            break


