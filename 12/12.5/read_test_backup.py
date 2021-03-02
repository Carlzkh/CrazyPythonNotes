f = open("read_test.py", 'r', True, encoding='utf-8')
while True:
    # 每次读取一个字符
    ch = f.read(3)
    # 如果没有读到数据，跳出循环
    if not ch:
        break
    # 输出ch
    print(ch, end='***')
f.close()
