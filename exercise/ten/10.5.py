"""
5.提示用户输入一个字符串和一个子串，打印出该子串在字符串中出现的 start 和 end 位置；
如果没有出现，则打印(-1,-1)。例如用户输入
aaadaa
aa
程序输出：
(0, 1)
(1, 2)
(4, 5)
"""
import re
strings = input('输入一个字符串：')
sub_str = input('输入一个子串：')
m1 = re.search(sub_str, strings)
if m1 is not None:
    print(m1.span())
else:
    print((-1, -1))
