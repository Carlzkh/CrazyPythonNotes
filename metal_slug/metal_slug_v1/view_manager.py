import pygame


class ViewManager:
    def __init__(self):
        self.screen_width = 1660
        self.screen_height = 1000
        # 保存角色生命值的成员变量
        x = self.screen_width * 15/100
        y = self.screen_height * 75/100
        # 控制角色的默认坐标
        self.X_DEFAULT = x
        self.Y_DEFALUT = y
        self.Y_JUMP_MAX = self.screen_height * 50/100

        self.map = pygame.image.load('images/map.jpg')
        self.map_back = pygame.image.load('images/game_back.jpg')
        self.map_back = pygame.transform.scale(self.map_back, (1980, 1240))
        # 加载角色站立时腿部动画帧的图片
        self.leg_stand_images = []
        self.leg_stand_images.append(pygame.image.load('images/leg_stand.png'))
        # 加载角色站立时头部动画帧的图片
        self.head_stand_images = []
        self.head_stand_images.append(pygame.image.load('images/head_stand_1.png'))
        self.head_stand_images.append(pygame.image.load('images/head_stand_2.png'))
        self.head_stand_images.append(pygame.image.load('images/head_stand_3.png'))
        # 加载角色跑动时腿部动画的图片
        self.leg_run_images = []
        self.leg_run_images.append(pygame.image.load('images/leg_run_1.png'))
        self.leg_run_images.append(pygame.image.load('images/leg_run_2.png'))
        self.leg_run_images.append(pygame.image.load('images/leg_run_3.png'))
        # 加载角色跑动时头部动画帧的图片
        self.head_run_images = []
        self.head_run_images.append(pygame.image.load("images/head_run_1.png"))
        self.head_run_images.append(pygame.image.load("images/head_run_2.png"))
        self.head_run_images.append(pygame.image.load("images/head_run_3.png"))
        # 加载角色跳跃腿部动画图片
        self.leg_jump_images = []
        self.leg_jump_images.append(pygame.image.load('images/leg_jump_1.png'))
        self.leg_jump_images.append(pygame.image.load('images/leg_jump_2.png'))
        self.leg_jump_images.append(pygame.image.load('images/leg_jump_3.png'))
        self.leg_jump_images.append(pygame.image.load('images/leg_jump_4.png'))
        self.leg_jump_images.append(pygame.image.load('images/leg_jump_5.png'))
        # 加载角色跳跃头部动画帧的图片
        self.head_jump_images = []
        self.head_jump_images.append(pygame.image.load('images/head_jump_1.png'))
        self.head_jump_images.append(pygame.image.load('images/head_jump_2.png'))
        self.head_jump_images.append(pygame.image.load('images/head_jump_3.png'))
        self.head_jump_images.append(pygame.image.load('images/head_jump_4.png'))
        self.head_jump_images.append(pygame.image.load('images/head_jump_5.png'))
        # 加载角色射击头部动画帧的图片
        self.head_shoot_images = []
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_1.png'))
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_2.png'))
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_3.png'))
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_4.png'))
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_5.png'))
        self.head_shoot_images.append(pygame.image.load('images/head_shoot_6.png'))
        # 加载子弹图片
        self.bullet_images = []
        self.bullet_images.append(pygame.image.load('images/bullet_1.png'))
        self.bullet_images.append(pygame.image.load('images/bullet_2.png'))
        self.bullet_images.append(pygame.image.load('images/bullet_3.png'))
        self.bullet_images.append(pygame.image.load('images/bullet_4.png'))
        self.head = pygame.image.load('images/head.png')
        # 加载第一种怪物未爆炸时的图片
        self.bomb_images = []
        self.bomb_images.append(pygame.image.load('images/bomb_1.png'))
        self.bomb_images.append(pygame.image.load('images/bomb_2.png'))
        # 加载第一种怪物爆炸时的图片
        self.bomb2_images = []
        self.bomb2_images.append(pygame.image.load('images/bomb2_1.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_2.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_3.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_4.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_5.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_6.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_7.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_8.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_9.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_10.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_11.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_12.png'))
        self.bomb2_images.append(pygame.image.load('images/bomb2_13.png'))
        # 加载第2种怪物(feiji)的图片
        self.fly_images = []
        self.fly_images.append(pygame.image.load('images/fly_1.png'))
        self.fly_images.append(pygame.image.load('images/fly_2.png'))
        self.fly_images.append(pygame.image.load('images/fly_3.png'))
        self.fly_images.append(pygame.image.load('images/fly_4.png'))
        self.fly_images.append(pygame.image.load('images/fly_5.png'))
        self.fly_images.append(pygame.image.load('images/fly_6.png'))
        # 加载第2种怪物(feiji)爆炸时的图片
        self.fly_die_images = []
        self.fly_die_images.append(pygame.image.load('images/fly_die_1.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_2.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_3.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_4.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_5.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_6.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_7.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_8.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_9.png'))
        self.fly_die_images.append(pygame.image.load('images/fly_die_10.png'))
        # 加载第3种怪物(ren)的图片
        self.man_images = []
        self.man_images.append(pygame.image.load('images/man_1.png'))
        self.man_images.append(pygame.image.load('images/man_2.png'))
        self.man_images.append(pygame.image.load('images/man_3.png'))
        # 加载第3种怪物(ren)死亡的图片
        self.man_die_images = []
        self.man_die_images.append(pygame.image.load('images/man_die_1.png'))
        self.man_die_images.append(pygame.image.load('images/man_die_2.png'))
        self.man_die_images.append(pygame.image.load('images/man_die_3.png'))
