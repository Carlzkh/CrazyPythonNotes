"""
4. 从标准输入读取两个整数并打印三行，其中第一行包含两个数的和；第二行包含两个数的
差（第一个数减第二个数）：第三行包含两个数的乘积结果
"""
a = input('输入第一个数A：')
b = input('输入第二个数B：')
print("AB的和: %d" % (int(a) + int(b)), end='\n')
print("AB的差: %d" % (int(a) - int(b)), end='\n')
print("AB的积: %d" % (int(a) * int(b)), end='\n')


