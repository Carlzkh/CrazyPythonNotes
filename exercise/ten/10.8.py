"""
8. 计算用户输入的两个带时区的时间戳字符串之间相差的秒数。例如用户输入：
Sun 10 May 2015 13:54:36 - 0700
Sun 10 May 2015 13:54:36 - 0000
程序应该输出：
25200
"""
import time
string_time1 = input('输入时间1：')
string_time2 = input('输入时间2：')
# string_time1 = 'Sun 10 May 2015 13:54:36 - 0700'
# string_time2 = 'Sun 10 May 2015 13:54:36 - 0000'
string_time1_slice = string_time1[:-7]
string_time2_slice = string_time2[:-7]
string_time1_zone = string_time1[-4:-2]
string_time2_zone = string_time2[-4:-2]

struct_time1 = time.strptime(string_time1_slice, '%a %d %b %Y %H:%M:%S')
struct_time2 = time.strptime(string_time2_slice, '%a %d %b %Y %H:%M:%S')
print(struct_time1)
time1_sec = int(time.mktime(struct_time1)) + int(string_time1_zone) * 3600
time2_sec = int(time.mktime(struct_time2)) + int(string_time2_zone) * 3600
print(time1_sec - time2_sec)
