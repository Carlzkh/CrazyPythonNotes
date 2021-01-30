"""
10. 打印出如下所示的近似圆，只要给定不同的半径，圆的大小就会随之发生改变（如果需要
使用复杂的数学运算 ，则可使 Python math 模块）
              * *
       *                 *
    *                       *
  *                            *
  *                            *
  *                            *
  *                            *
   *                          *
      *                    *
         *               *
                * *

"""
import turtle
import math
window = turtle.Turtle()


def c(windows, r, angle):
    height = 2 * math.pi * r / 360
    for i in range(angle):
        windows.fd(height)
        windows.lt(1)


c(window, 100, 360)

#怎么测试自己代码话的圆半径为100？
#window.lt(90)
#window.fd(100)
#window.lt(90)
#window.fd(100)
#将这4句代码添加即可
# turtle.mainloop()

