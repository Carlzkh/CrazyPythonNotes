"""
2. 提示用户不断地输入多行内容，程序自动将该内容保存到 my.txt 文件中 到用 户输入 exit
为止
"""
while True:
    i = input('输入exit退出')
    if i == 'exit':
        break
    else:
        with open('my.txt', 'a+') as f:
            f.write(i + '\n')
