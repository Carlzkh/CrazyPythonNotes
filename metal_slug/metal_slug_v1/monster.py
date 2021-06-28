import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

COMMON_SPEED_THRESHOLD = 6
MAN_SPEED_THRESHOLD = 4

TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3


class Monster(Sprite):
    def __init__(self, view_manager, tp=TYPE_BOMB):
        super().__init__()
        self.type = tp
        self.x = 0
        self.y = 0
        self.is_die = False
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.draw_count = 0
        self.draw_index = 0
        self.die_max_draw_count = sys.maxsize
        self.bullet_list = Group()
        if self.type == TYPE_BOMB or self.type == TYPE_MAN:
            self.y = view_manager.Y_DEFALUT
        elif self.type == TYPE_FLY:
            self.y = view_manager.screen_height * 50 / 100 - randint(0, 99)
        self.x = view_manager.screen_width + randint(0, view_manager.screen_width >> 1) - (
                view_manager.screen_width >> 2)

    # 绘制怪物的方法
    def draw(self, screen, view_manager):
        if self.type == TYPE_BOMB:
            self.draw_anim(screen, view_manager,
                           view_manager.bomb2_images if self.is_die else view_manager.bomb_images)
        elif self.type == TYPE_FLY:
            self.draw_anim(screen, view_manager,
                           view_manager.fly_die_images if self.is_die else view_manager.fly_images)
        elif self.type == TYPE_MAN:
            self.draw_anim(screen, view_manager,
                           view_manager.man_die_images if self.is_die else view_manager.man_images)
        else:
            pass

    def draw_anim(self, screen, view_manager, bitmap_arr):
        if self.is_die and self.die_max_draw_count == sys.maxsize:
            self.die_max_draw_count = len(bitmap_arr)
        self.draw_index %= len(bitmap_arr)
        bitmap = bitmap_arr[self.draw_index]
        if bitmap is None:
            return
        draw_x = self.x
        if self.is_die:
            if type == TYPE_BOMB:
                draw_x = self.x - 50
            elif type == TYPE_MAN:
                draw_x = self.x + 50
        draw_y = self.y - bitmap.get_height()
        screen.blit(bitmap, (draw_x, draw_y))
        self.start_x = draw_x
        self.start_y = draw_y
        self.end_x = self.start_x + bitmap.get_width()
        self.end_y = self.start_y + bitmap.get_height()
        self.draw_count += 1
        # 控制人、飞机发射子弹的速度
        if self.draw_count >= (COMMON_SPEED_THRESHOLD if type == TYPE_MAN else MAN_SPEED_THRESHOLD):
            # 如果怪物是入，则只在第民才发射子惮
            if self.type == TYPE_MAN and self.draw_index == 2:
                self.add_bullet()
            # 如果怪物是飞机，则只在最后一帧才发射子弹
            if self.type == TYPE_FLY and self.draw_index == len(bitmap_arr) - 1:
                self.add_bullet()
            self.draw_index += 1
            self.draw_count = 0

        if self.is_die:
            self.die_max_draw_count -= 1
        # 绘制子弹
        self.draw_bullets(screen, view_manager)

    def is_hurt(self, x, y):
        return self.start_x < x < self.end_x and self.start_y < y < self.end_y

    # 根据怪物类型获取子弹类型，不同怪物发射不同的子弹
    # return 代表这种怪物不发射子弹
    def bullet_type(self):
        if self.type == TYPE_BOMB:
            return 0
        elif self.type == TYPE_FLY:
            return BULLET_TYPE_3
        elif self.type == TYPE_MAN:
            return BULLET_TYPE_2
        else:
            return 0

    def add_bullet(self):
        # 如果没有子弹
        if self.bullet_type() <= 0:
            return
        # 计算子弹的坐标
        draw_x = self.x
        draw_y = self.y - 60
        # 如果怪物是飞机，则重新计算飞机发射的子弹的坐标
        if self.type == TYPE_FLY:
            draw_y = self.y - 30
        # 创建子弹对象
        bullet = Bullet(self.bullet_type(), draw_x, draw_y, Player.DIR_LEFT)
        # 将子弹对象添加到该怪物发射的子弹Group
        self.bullet_list.add(bullet)

    # 更新所有子弹的位置：将所有子弹的坐标减少shift距离（子弹左移）
    def update_shift(self, shift):
        self.x -= shift
        for bullet in self.bullet_list:
            if bullet is not None:
                bullet.x -= shift

    # 绘制子弹的方法

    def draw_bullets(self, screen, view_manager):
        # 遍历该怪物发射的所有子弹
        for bullet in self.bullet_list.copy():
            # 如果子弹己经越过屏幕
            if bullet.x <= 0 or bullet.x > view_manager.screen_width:
                # 删除已经移出屏幕的子弹
                self.bullet_list.remove(bullet)
        # 绘制所有子弹
        for bullet in self.bullet_list.sprites():
            # 获取子弹对应的位图
            bitmap = bullet.bitmap(view_manager)
            if bitmap is None:
                continue
            # 子弹移动
            bullet.move()
            # 绘制子弹位图
            screen.blit(bitmap, (bullet.x, bullet.y))
