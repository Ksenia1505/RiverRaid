import pygame
import background
import plane
import ship
import function
import database
import sys
from tkinter import *
from tkinter import messagebox

# Главный файл игры
pygame.init()

# предварительные настройки
background_image = pygame.image.load('images/levels/level_1a.png')
plane_image = pygame.image.load('images/plane1.png')
bg_speed = 4
width = background_image.get_size()[0]
height = background_image.get_size()[1]
window_height = 700
bg_x = 0
bg_y = window_height - height
plane_w = plane_image.get_size()[0]
plane_h = plane_image.get_size()[1]
plane_x = width // 2 - plane_w // 2
plane_y = window_height - plane_h - 10
window = pygame.display.set_mode((width, window_height))

pygame.display.set_caption('River Raid')

clock = pygame.time.Clock()
background = background.Background(bg_x, bg_y, bg_speed, width, height, window, background_image)
plane = plane.Plane(plane_x, plane_y, window, width, window_height, plane_w, plane_h, plane_image)

# получение кораблей
ships = []
database = database.Database()
for coordinates in database.get_coordinates('ship'):
    ships.append(ship.Ship(coordinates[0], coordinates[1], window, width, coordinates[3], coordinates[2]))

animCount = 0
run = True
bullets = []
lastMove = ''

# главный цикл игры
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    background.draw()
    pygame.draw.rect(window, (200, 200, 200),
                     (plane.x, plane.y, plane.w, plane.h))
    plane.draw()

    for ship in ships:
        if ship.enabled and \
                ship.start_y <= (background.height + background.y) and \
                ship.y < window_height:
            pygame.draw.rect(window, (255, 255, 255),
                             (ship.x, ship.y, ship.w, ship.h))
            ship.draw()

            # проверка на столкновение самолета и корабля
            if function.is_plane_collided_with_ship(plane, ship):
                Tk().wm_withdraw()
                messagebox.showinfo('Столкновение!', 'Вы проиграли')
                sys.exit()

            # обработка выстрела
            counter = 1
            while counter <= 5:
                if plane.shell.x != -1:
                    plane.shell.draw()
                    if plane.shell.y > plane.shell.radius:
                        plane.shell.y -= plane.shell.radius
                    else:
                        plane.shell.x = -1

                # проверка попадания выстрела в корабль
                if plane.shell.x != -1:
                    if plane.shell.x != -1 and function.is_shell_collided_with_ship(plane.shell, ship):
                        ship.enabled = False
                        plane.shell.x = -1

                counter += 1

            # движение корабля вниз
            ship.y += bg_speed

            # обработка горизонтального движения корабля
            if ship.direction == 'left':
                ship.x = max(0, ship.x - ship.speed_x)
                if ship.x == 0:
                    ship.direction = 'right'
            else:
                ship.x = min(width - ship.w, ship.x + ship.speed_x)
                if ship.x == width - ship.w:
                    ship.direction = 'left'

    pygame.display.update()

pygame.quit()
