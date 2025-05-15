"""Функционал корабля"""

import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Инициализируем корабль"""
        self.screen = screen

        temp_image = pygame.image.load("images\ship.bmp")
        self.image = pygame.transform.scale(temp_image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
         
        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.ai_settings = ai_settings

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor  

        if self.center < 0:
            self.center = 0
        elif self.center > 1200:
            self.center = 1200 

    def blitme(self):
        """Рисует корабль"""
        self.rect.centerx = self.center
        self.screen.blit(self.image, self.rect)

        