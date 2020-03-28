"""
控制循环结构

"""

'''
1、break提前终止循环，不需要等条件false
for...else... 中遇到break将不执行else，直接跳出所有循环

'''
for i in range(10):
    print('i的值：', i)
    if i == 2:
        break
        print('jiehsu')


for i in range(10):
    print('i的值：', i)
    if i == 2:
        break
    else:
        print('i = 2时此处将不被执行')


'''
2、continue
忽略本次循环后的代码，直接进行下一次循环前的判断
'''

for i in range(3):
    print('i的值：', i)
    if i == 1:
        continue
    print('i = 1 时将不被执行')


'''
3、return
return直接结束函数或方法，不管循环嵌套多少层，全部结束

'''

























