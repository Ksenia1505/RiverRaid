import pygame

class Ship:
    def __init__(self, x, y, window, window_width, direction, start_y):
        self.x = x
        self.y = y
        self.window = window
        self.window_width = window_width
        self.direction = direction
        self.start_y = start_y

        self.w = 120
        self.h = 150
        self.speed_x = 10
        self.enabled = True
        self.ship_image = pygame.image.load('images/ship.png')

        self.point_1 = []
        self.point_2 = []
        self.point_3 = []
        self.point_4 = []


    def draw(self):
        self.window.blit(self.ship_image, (self.x, self.y))
