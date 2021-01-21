"""
3. 定义 1个正 表达式，用于验证国内的所有手机号码
"""
import re
tel = input("请输入手机号:")
# ret = re.match(r"1[35678]\d{9}", tel)
# 由于手机号位数大于11位也能匹配成功，所以修改如下：
ret = re.match(r"^1[35678]\d{9}$", tel)

if ret:
    print("匹配成功")
else:
    print("匹配失败")
