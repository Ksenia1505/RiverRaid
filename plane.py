import pygame
import shell

class Plane:
    def __init__(self, x, y, window, window_width, window_height, w, h, plane_image):
        self.x = x
        self.y = y
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.w = w
        self.h = h

        self.shell = shell.Shell(-1, -1, self.window_height, self.window)
        self.plane_image = plane_image


    def draw(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = max(self.x - 7, 5)
        elif keys[pygame.K_RIGHT]:
            self.x = min(self.x + 7, self.window_width - 5 - self.w)
        elif keys[pygame.K_SPACE]:
            if self.shell.x == -1:
                self.shell = shell.Shell(self.x + self.w // 2, self.window_height - self.h, self.window_height, self.window)
        self.window.blit(self.plane_image, (self.x, self.y))






