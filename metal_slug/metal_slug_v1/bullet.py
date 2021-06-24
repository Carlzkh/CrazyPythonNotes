import pygame
from pygame.sprite import Sprite
import player
# 定义代表子弹 型的常量（ 如果程 需要增加更 的子弹，则只需在此处添加常量即可）
BULLET_TYPE_1 = 1
BULLET_TYPE_2 = 2
BULLET_TYPE_3 = 3
BULLET_TYPE_4 = 4


class Bullet (Sprite):
    def __init__(self, tipe, x, y, pdir):
        super().__init__()
        # 定义 弹的类型
        self.type = tipe
        # 子弹的 坐标
        self.x = x
        self.y = y
        # 定义子弹的射击方向
        self.dir = pdir
        # 定义子弹在 方向上的加速度
        self.y_accelate = 0
        # 子弹是否有效
        self.is_effect = True

    # 根据子弹类型来获取对应的位图

    def bitmap(self, view_manager):
        return view_manager.bullet_images[self.type - 1]

    # 根据子弹类型来计算子弹在方向上的速度

    def speed_x(self):
        # 根据玩家的方向来计算子弹方向和移动方向
        sign = 1 if self.dir == player.DIR_RIGHT else -1
        # 对于第种子弹，以12为基数来计算其速度
        if self.type == BULLET_TYPE_1:
            return 12 * sign
        # 对于第种子弹，以为基数来计算其速度
        elif self.type == BULLET_TYPE_2:
            return 8 * sign
        # 对于第种子弹，以为基数来计算其速度
        elif self.type == BULLET_TYPE_3:
            return 8 * sign
        # 对于第种子弹，以为基数来计算其速度
        elif self.type == BULLET_TYPE_4:
            return 8 * sign
        else:
            return 8 * sign

    # 根据子弹类型来计算子弹在方向上的速度

    def speed_y(self):
        # 如果selfy_accelate不为 ，贝self.y_accelate作为方向上的速度

        if self.y_accelate != 0:
            return self.y_accelate
        # 此处控制只有第种子弹才有方向上的速度（子弹会斜着向下移动〉
        if self.type == BULLET_TYPE_1 or self.type == BULLET_TYPE_2 or self.type == BULLET_TYPE_4:
            return 0
        elif self.type == BULLET_TYPE_3:
            return 6
