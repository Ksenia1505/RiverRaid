import pygame


class Shell:
    def __init__(self, x, y, window_height, window):
        self.x = x
        self.y = y
        self.window_height = window_height
        self.window = window

        self.color = (255, 34, 144)
        self.background_color = (0, 163, 233)
        self.radius = 3

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
        # pygame.draw.circle(self.window, self.background_color, (self.x, self.y + self.radius * 2), self.radius)
