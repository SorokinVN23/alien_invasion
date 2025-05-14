
import sys

import pygame

def check_events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

def update_screen(ship):
    ship.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()          