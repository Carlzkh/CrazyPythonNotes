import sys
import re

# 定义匹配Email的正则表达式
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?'
# 读取标准输入
text = sys.stdin.read()  # 文件需要是utf-8编码格式的！
print(text)
# 使用正则表达式执行查找

it = re.finditer(mailPattern, text, re.I)
# 输出所有的电子邮件
for e in it:
    print(str(e.span()) + "-->" + e.group())


# 控制台执行命令：type ad.txt | python pipein_test.py
# 管道符'|'前面的命令type ad.txt的输出，会作为后面的命令python pipein_test.py的输入。
