"""
2. 开发并完善本章介绍的桌面弹球游戏 为桌面弹球游戏增加一些障碍物
"""
import tkinter
from tkinter import *
import threading
import random
from tkinter import messagebox

GAME_WIDTH = 500
GAME_HEIGHT = 680
BOARD_X = 230
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 30


class App:
    def __init__(self, master):
        self.master = master
        # 记录小球动画的第几
        self.ball_index = 0
        # 记录游戏是否失败的旗标
        self.is_lose = False
        # 初始化记录小球位置的变量
        self.cur_x = 260
        self.cur_y = 30
        self.board_x = BOARD_X
        self.cv = Canvas(root, background='white', width=GAME_WIDTH, height=GAME_HEIGHT)
        self.bms = []
        self.init_widgets()
        self.ball = self.cv.create_image(self.cur_x, self.cur_y, image=self.bms[self.ball_index])
        self.board = self.cv.create_rectangle(BOARD_X, BOARD_Y, BOARD_X + BOARD_WIDTH,
                                              BOARD_Y + 20, width=0, fill='light blue')
        self.vx = random.randint(6, 10)  # 方向的速度
        self.vy = random.randint(8, 12)  # 方向的速度
        # 通过定时器指定 O.ls 之后执行 move_ball 阪数
        self.t = threading.Timer(0.1, self.move_ball)
        self.t.start()

    # 创建界面组件
    def init_widgets(self):

        self.cv.pack()
        # 让画布得到焦点，从而可以响应按键事件
        self.cv.focus_set()

        # 初始化小球的动画帧
        for i in range(8):
            self.bms.append(PhotoImage(file='images/ball' + str(i+1) + '.png'))
        # 绘制小球

        # 为向左箭头绑定事件处理函数，拍板左移
        self.cv.bind('<Left>', self.move_left)
        # 为向右箭头绑定事件处理函数，挡板右移
        self.cv.bind('<Right>', self.move_right)

    def move_left(self, event):
        if self.board_x <= 0:
            return
        self.board_x -= 15
        self.cv.coords(self.board, self.board_x, BOARD_Y, self.board_x + BOARD_WIDTH, BOARD_Y + 20)

    def move_right(self, event):
        if self.board_x + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.board_x += 15
        self.cv.coords(self.board, self.board_x, BOARD_Y, self.board_x + BOARD_WIDTH, BOARD_Y + 20)

    def move_ball(self):
        self.cur_x += self.vx
        self.cur_y += self.vy
        # 小球到了右边墙壁，转向
        if self.cur_x + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        # 小球到了左边墙壁，转向
        if self.cur_x - BALL_RADIUS <= 0:
            self.vx = -self.vx
        # 小球到了上边墙壁 转向
        if self.cur_y - BALL_RADIUS <= 0:
            self.vy = -self.vy
        # 小球到了挡板处
        if self.cur_y + BALL_RADIUS >= BOARD_Y:
            # 如果在挡板范围内
            if self.board_x <= self.cur_x <= (self.board_x + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title='失败', message='您己 输了')
                self.is_lose = True
        self.cv.coords(self.ball, self.cur_x, self.cur_y)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.bms[self .ball_index % 8])
        # 如果游戏还未失败，让定时器继续执行
        if not self.is_lose:
            # 通过定时器指定 ls 之后执行move_ball 函数
            self.t = threading.Timer(0.1, self.move_ball)
            self.t.start()


root = Tk()
root.title('弹球游戏')
root.iconbitmap('images/fk_logo.ico')
root.geometry('%dx%d' % (GAME_WIDTH, GAME_HEIGHT))
# 禁止改变窗口大小
root.resizable(width=False, height=False)
App(root)
root.mainloop()
