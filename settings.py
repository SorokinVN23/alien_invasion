"""Модуль с настройками"""

class Settings():
    """Класс настроек"""

    def __init__(self):
        """Инициализирует настройки"""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5