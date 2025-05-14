import time

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  # Инициализирует игру и создает объект экрана.
  pygame.init()

  ai_settings = Settings()
  

  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  screen.fill(ai_settings.bg_color)
  ship = Ship(screen)

  # Запуск основного цикла игры.
  while True:
    gf.check_events()
    
    gf.update_screen(ship)

    time.sleep(0.1)

run_game()