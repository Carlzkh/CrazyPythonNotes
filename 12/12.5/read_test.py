f = open("read_test.py", 'rb', True)
while True:
    # 每次读取一个字符
    ch = f.read().decode('utf8')
    # 如果没有读到数据，跳出循环
    if not ch:
        break
    # 输出ch
    print(ch, end='')
f.close()
