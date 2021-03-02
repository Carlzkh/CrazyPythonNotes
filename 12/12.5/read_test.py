# f = open("read_test.py", 'rb', True)
# while True:
#     # 每次读取一个字符
#     ch = f.read().decode('utf8')
#     # 如果没有读到数据，跳出循环
#     if not ch:
#         break
#     # 输出ch
#     print(ch, end='')
# f.close()

f = open("read_test.py", "rb")  # 二进制格式读文件
while True:
    line = f.read(3)
    if not line:
        break
    else:
        try:
            print(line.decode('utf8'))
            line.decode('utf8')
            # 为了暴露出错误，最好此处不print
        except UnicodeDecodeError as e:
            print('error', str(line))
