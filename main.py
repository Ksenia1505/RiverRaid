import pygame
import background
import plane
import ship

pygame.init()
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
direction = 'left'
ship_x = width - 500
ship_y = 0
ship = ship.Ship(ship_x, ship_y, window, width, direction)

animCount = 0
run = True
bullets = []
lastMove = ''

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    background.draw()
    plane.draw()

    if plane.shell.x != -1:
        plane.shell.draw()
        if plane.shell.y > plane.shell.radius * 5:
            plane.shell.y -= plane.shell.radius * 5
        else:
            plane.shell.x = -1

    if ship.enabled:
        ship.draw()
        ship.y += bg_speed
        if ship.direction == 'left':
            ship.x = max(0, ship.x - ship.speed_x)
            if ship.x == 0:
                ship.direction = 'right'
        else:
            ship.x = min(width - ship.width, ship.x + ship.speed_x)
            if ship.x == width - ship.width:
                ship.direction = 'left'

    pygame.display.update()

pygame.quit()
