"""
12. 完善数字转人民币读法的程序。

"""

'''
把一个浮点数分解成整数部分和小数部分字符串
num 是需要被分解的浮点数
返回分解出来的整数部分和小数部分
第一个数组元素是整数部分，第二个数组元素是小数部分
'''


def divide(num1):
    # 将一个浮点数强制类型转换为 int 类型， 即得到它的整数部分
    integer1 = int(num1)
    # 浮点数减去整数部分，得到小数部分，小数部分乘以 100 后再取整 得到 位小数
    fraction1 = round((num1 - integer1) * 100)
    # 下面把整数转换为字符串
    return str(integer1), str(fraction1)


han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit_list = ['十', '百', '千']

'''
把一个4位的数字字符串变成汉字字符串
num_str 是需要被转换的4位数字字符串
返回4位数字字符串被转换成汉字字符串
'''


def four_to_chinese_str(num_str):
    result = ""
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转换成数值
        num1 = int(num_str[i])
        # 如果不是最后一位数字 而且数字不是零，则需要添加单位（千、百、十）
        if i != num_len - 1:
            if num1 != 0:
                result += han_list[num1] + unit_list[num_len-2-i]
            else:
                if num_str[i+1] == '0':
                    pass
                else:
                    result += han_list[num1]
        # 否则不要添加单位
        # elif num_str[i-1] == '0' and num_str[i] == '0':
        #    pass
        else:
            if num1 != 0:
                result += han_list[num1]
            else:
                pass
    return result


def fraction_to_chinese_str(fraction1):
    num1 = int(fraction1[0])
    num2 = int(fraction1[1])
    return han_list[num1]+'角'+han_list[num2]+'分'


'''
数字字符串变成汉字字符串
num_ tr 是需要被转换的数字字符串
返回数字字符串被转换成汉字字符串
'''


def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大，翻译不了')
        return
    # 如果大于8，包含单位 “亿”
    elif str_len > 8:
        return four_to_chinese_str(num_str[:-8])+'亿' +\
            four_to_chinese_str(num_str[-8:-4])+'萬' +\
            four_to_chinese_str(num_str[-4:])+'元'
    # 如果大于4位，包含单位“万”
    elif str_len > 4:
        return four_to_chinese_str(num_str[:-4])+'萬' +\
            four_to_chinese_str(num_str[-4:])+'元'
    else:
        return four_to_chinese_str(num_str)+'元'


def fraction_to_str(fraction1):
    # fraction1 = divide(num_str)[1]
    return fraction_to_chinese_str(fraction1)


num = float(input('请输入一个浮点数 ：'))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(num)
# 测试把一个 位的数字字符串变成汉字字符串
# print(integer_to_str(integer))
# print(integer, fraction)
# print(fraction_to_chinese_str(fraction))
print(integer_to_str(integer)+fraction_to_chinese_str(fraction))


















