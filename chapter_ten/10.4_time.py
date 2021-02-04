import time

print(time.asctime())  # 将时间元组或struct_time转换成时间字符串，不带参数就是转换当前时间
print(time.asctime((2018, 5, 2, 8, 0, 30, 0, 51, 1)))
print(type(time.asctime()))
print(time.ctime(1558653254))  # 将秒数转化成时间字符串
print(time.ctime(30))  # 将秒数转化成时间字符串，会计算时区，所以中国是1970-01-01 08:00:30
print(time.gmtime())  # 将秒数转化成struct_time对象，不填参数就是当前时间，没有时区（输出时间比中国时区当前时间早8小时）
print(time.localtime())  # 将秒数转化成struct_time对象，不填参数就是当前时间，有时区

print(time.mktime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))  # 1517713703.0 # 将元组格式或struct_time的时间转换为秒数代表的时间

print(time.perf_counter())  # 返回性能计数器的值

print(time.process_time())  # 返回当前进程使用CPU的时间
# time.sleep(10)

print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 将当前时间转换为指定格式的字符串,带时区
st = '2018年3月20日'

print(time.strptime(st, '%Y年%m月%d日'))  # 将指定时间字符串恢复成struct_time对象。

print(time.time())  # 返回从1970年1月1日0点整到现在过了多少秒。

print(time.timezone)  # 在国内东八区输出-28800  # 返回本地时区的时间偏移，以秒为单位
print(time.tzname)  # 返回本地时区的名字
a = time.tzname[0]
c = time.tzname[1]
b = a.encode('latin-1').decode('gb2312')
d = c.encode('latin-1').decode('gbk')
# e = bytes(a).decode('gbk')
print(b, d)
