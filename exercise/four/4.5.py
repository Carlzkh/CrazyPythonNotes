"""
5. 使用循环输出空心菱形 例如用户输入 7（用户输入偶数， 提示不能打印) 输出如下结果：
   *
  * *
 *   *
*     *
 *   *
  * *
   *

"""
n = int(input('输入一个奇数：'))
if n % 2 != 0:
    for i in range(1, n+1):
        if i == 1:
            print(' '*((n+1)//2-i), end='')
            print('*', end='')
            print(' '*(2*i-1-2))
        elif i < (n+1) / 2:
            print(' '*((n+1)//2-i), end='')
            print('*', end='')
            print(' '*(2*i-1-2), end='')
            print('*')
        elif i == (n+1) / 2:
            print('*', end='')
            print(' '*(2*i-1-2), end='')
            print('*')
        elif n > i > (n+1)/2:
            print(' '*(i-(n+1)//2), end='')
            print('*', end='')
            print(' '*(2*(n-i)-1), end='')
            print('*')
        else:
            print(' '*(i-(n+1)//2), end='')
            print('*', end='')
            print(' '*(2*(n-i)-1))
else:
    print('用户输入的是偶数，不能打印！')
