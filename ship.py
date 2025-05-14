"""Функционал корабля"""

import pygame

class Ship():

    def __init__(self, screen):
        """Инициализируем корабль"""
        self.screen = screen

        temp_image = pygame.image.load("images\ship.bmp")
        self.image = pygame.transform.scale(temp_image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)

        