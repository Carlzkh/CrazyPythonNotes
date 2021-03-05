"""
seek(offest[,whence]):offest是偏移量，
    whence=0时代表从文件开头计算，默认是0
    whence=1时代表从当前位置计算，默认是0
    whence=2时代表从文件结尾计算，默认是0
"""
f = open('filept_test.py', 'rb')
# 判断文件指针的位置
print(f.tell())  # 0
# 将文件指针移动到3处
f.seek(3)
print(f.tell())  # 3
# 读取一个字节，文件指针自动后移1个数据
print(f.read(36).decode('utf-8'))  # 30个字节后刚好到汉字，需要加3的倍数的偏移量
print(f.tell())  # 4
# 将文件指针移动到5处
f.seek(5)
print(f.tell())  # 5
# 将文件指针向后移动5个数据
f.seek(5, 1)
print(f.tell())  # 10
# 将文件指针移动到倒数第10处
f.seek(-11, 2)  # 解码后若读的是中文则三个b为一个字符，千万要注意utf-8中文是三个字节！
print(f.tell())
print(f.read().decode('utf-8'))  # d,换行算两个偏移量(即占两个字节，/r/n)防报错大法
