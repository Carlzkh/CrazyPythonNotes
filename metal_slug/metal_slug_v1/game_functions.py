import sys
import pygame


def check_events(screen, view_manager):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, view_manager, mm):
    mm.generate_monster(view_manager)
    screen.blit(view_manager.map, (0, 0))
    mm.draw_monster(screen, view_manager)
    pygame.display.flip()
