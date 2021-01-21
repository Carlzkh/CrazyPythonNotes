"""
8. 计算用户输入的两个带时区的时间戳字符串之间相差的秒数。例如用户输入：
Sun 10 May 2015 13:54:36 - 0700
Sun 10 May 2015 13:54:36 - 0000
程序应该输出：
25200
"""
import time
print(7*3600)
string1 = 'Sun 10 May 2015 13:54:36'
struct_time_one = time.strptime(string1, '%a %d %b %Y %H:%M:%S')
print(struct_time_one)
