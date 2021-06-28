import pygame
import sys
from view_manager import ViewManager
import game_functions as gf
import monster_manager as mm


def run_game():
    pygame.init()
    view_manager = ViewManager()
    screen = pygame.display.set_mode((view_manager.screen_width, view_manager.screen_height))
    pygame.display.set_caption("合金弹头")

    while True:
        gf.check_events(screen, view_manager)
        gf.update_screen(screen, view_manager, mm)


run_game()
