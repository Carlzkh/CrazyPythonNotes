"""1. 使用循环输出九九乘法表。输 出如下结果：
1 x 1 = 1
1 × 2 = 2, 2 × 2 = 4
1 × 3 = 3, 2 × 3 = 6, 3 × 3= 9
1 × 9 = 9, 2 × 9 = 18, 3 × 9 = 27, … , 9 x 9 = 81

"""
for i in range(1, 10):
    for j in range(1, i+1):
        print("%s × %s =" % (j, i), i*j, end='')
        if i != j:
            print(', ', end='')
    print(end="\n")
