import codecs
# 指定使用utf-8字符集读取文件内容
f = codecs.open("for_file.py", 'r', 'utf-8', buffering=True)
# 使用for循环遍历文件对象
for line in f:
    print(line, end='')
f.close()
# 将文件对象转换为list列表
print(list(codecs.open("for_file.py", 'r', 'utf-8', buffering=True)))
