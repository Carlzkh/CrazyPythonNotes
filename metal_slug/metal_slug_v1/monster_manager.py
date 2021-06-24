from monster import *


die_monster_list = Group()
monster_list = Group()


def generate_monster(view_manager):
    if len(monster_list) < 3 + randint(0, 2):
        monster = Monster(view_manager, randint(1, 3))
        monster_list.add(monster)


def update_posistion(screen, view_manager, player, shift):
    del_list = []
    for monster in monster_list.sprites():
        monster.draw_bullets(screen, view_manager)
        monster.update_shift(shift)
        if monster.x < 0:
            del_list.append(monster)
    monster_list.remove(del_list)
    del_list.clear()
    for monster in die_monster_list.sprites():
        monster.update_shift(shift)
        if monster.x < 0:
            del_list.append(monster)
    die_monster_list.remove(del_list)


# 绘制所有’怪物的函数
def draw_monster(screen, view_manager):
    # 遍历所有活着的怪物，绘制活着的怪物
    for monster in monster_list .sprites():
        # 绘制怪物
        monster.draw(screen, view_manager)
    del_list = []
    # 遍历所有已经死亡的怪物，绘制己经死亡的怪物
    for monster in die_monster_list .sprites():
        # 绘制怪物
        monster.draw(screen, view_manager)
        # 当怪物的 die_max draw_count 返回 时，表明该怪物已经死亡
        # 且该怪物的死亡动画的所有帧都播放完成 将它们彻底删除
        if monster.die_max_draw_count <= 0:
            del_list.append(monster)
    die_monster_list.remove(del_list)
