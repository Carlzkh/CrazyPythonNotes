import time

print(time.asctime())  # 将时间元组或struct_time转换成时间字符串，不带参数就是转换当前时间
print(time.asctime((2018, 5, 2, 8, 0, 30, 0, 51, 1)))
print(type(time.asctime()))
print(time.ctime(1558653254))  # 将秒数转化成时间字符串
print(time.ctime(30))  # 将秒数转化成时间字符串，会计算时区，所以中国是1970-01-01 08:00:30



