import pygame

class Ship:
    def __init__(self, x, y, window, window_width, direction):
        self.x = x
        self.y = y
        self.window = window
        self.window_width = window_width
        self.direction = direction

        self.width = 120
        self.speed_x = 10
        self.enabled = True
        self.ship_image = pygame.image.load('images/ship.png')


    def draw(self):
        self.window.blit(self.ship_image, (self.x, self.y))
