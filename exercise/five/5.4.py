"""
4. 定义一个 count_str_ char( my_ str1 ）函数，该函数返回参数字符串中包含多少个数字、 少个
英文字母、多少个空白字符、多少个其他字符
"""


def count_str_char(input_string):
    english = 0
    space = 0
    number = 0
    other = 0
    for i in range(len(input_string)):
        if input_string[i].isalpha():
            # print('这个是英文字母：', input_string[i])
            english += 1
        elif input_string[i].isdigit():
            # print('这个数字：', input_string[i])
            number += 1
        elif input_string[i].isspace():
            # print('这个是空格：', input_string[i])
            space += 1
        else:
            # print('这个是其他字符：', input_string[i])
            other += 1
    return english, space, number, other


input_string1 = input("输入一个字符串：")
english1, space1, number1, other1 = count_str_char(input_string1)
print('该字符串含英文字母%d个，空格%d个，数字%d个，其他字符%d个' % (english1, space1, number1, other1))
