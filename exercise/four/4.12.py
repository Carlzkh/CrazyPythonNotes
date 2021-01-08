"""
12. 完善数字转人民币读法的程序。

"""

”’ 个浮点数分解成整数部分和小数部分字符串
num 是需要被分解的浮点数
返回分解出来的整数部分和 数部分
个数组元素是整数部分，第 个数组元素是小数部分
def divide (num) :
＃将 个浮点数强制类型转换为 int 类型， llll 得到它的整数部分
integer= int(num)
＃浮点数减去整数部分，得到小数部分，小数部分乘以 100 后再取整 得到 位小数
fraction = round （（口 um - integer) * 100)
＃下面把整数转换为字符串
return (str(integer), str(fraction))
han_list ＝｛ ”，” ”，” ”，” ”，” ”，
”，”陆”，” ”，” ”，”
unit_list = ”，” ”，”千”
把一个 位的数字字符串变成汉字字符串
num str 是需要被转换的 位数字字符串
返回 位数字字符串被转换成汉字字符串
‘
86
仅供非商业用途或交流学习使用
WWW.，而ανα.org 章流程控制
def four to hanstr(num str) :
result = ""
num len = len(num str)
＃依次遍历数字字符串的每一位数字
for in range(num_len)
＃把字符串转换成数值
num = int(num str[i] )
＃如果不是最后一位数字 而且数字不是零，则需要添加单位（千、百、十）
if i != num len - 1 and num != 0
result += han list[num] +unit list[num len - 2 - i)
＃否则 要添加单位
else
result += han list[num]
return result
数字字符串变成汉字字符串
num_ tr 是需要被转换的数字字符串
返回数字字符串被转换成汉字字符串
def integer to str(num str):
str len = len(num str)
if str len > 12 :
print （’数 太大，翻译不了’）
return
＃如果大于 ，包含单位 “亿”
elif str len > 8 :
re turn four to hanstr （口 um str[: - 8] ) ＋＼
four to hanstr(num str[- 8 : - 4]) ＋＼
four to hanstr(num str(- 4 : ])
＃如果大于 位，包含单位“万”
elif str len > 4 :
return four to hanstr(num str( :-4]) ＋＼
four to hanstr(num str[-4:])
else :
return four to hanstr(num str)
num = float(input （”请输入一个浮点数 ：”）
＃测试把一个浮点数分解成整数部分和小数部分
integer, fraction = vide(num)
＃测试把一个 位的数字字符串变成汉字字符串
print(integer_t 。一str (integer))
print(fraction)
运行上面程序，将看


















