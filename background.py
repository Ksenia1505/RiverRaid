import pygame


class Background:
    def __init__(self, x, y, speed, width, height, window, background_image):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.window = window
        self.background_image = background_image
        self.boost = 0
        self.max_boost = 10

    def draw(self):
        self.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.boost += 1
            if self.boost > self.max_boost:
                self.boost = self.max_boost
        elif keys[pygame.K_DOWN]:
            self.boost -= 1
            if self.boost < 0:
                self.boost = 0
        self.y += self.boost
        if self.y <= 0:
            self.window.blit(pygame.transform.scale(self.background_image, (self.width, self.height)), (0, self.y))
