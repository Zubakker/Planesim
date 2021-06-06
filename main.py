import pygame

from math import atan2, sqrt, sin, cos
from time import time

from plane import Plane

plane = Plane()

SCREEN_SIZE = (700, 700)
CENTER = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 1m = 10 px
size = 10
d_ang = atan2(plane.height, plane.width)
diag = 0.5 * sqrt(plane.width**2 + plane.height**2)
last_frame = time()
zero = time()

while True:
    delta_t = time() - last_frame
    if time() - zero >= 1:
        print(plane.tile_y, plane.h_speed, plane.v_speed, plane.speed)
        zero = time()
    screen.fill((0,0,0))
    plane.calc(delta_t)
    dx = int(plane.tile_x * size)
    dy = int(plane.tile_y * size)

    a = int(diag * size * cos(plane.angle + d_ang))
    c = int(diag * size * cos(plane.angle - d_ang))
    b = int(diag * size * sin(plane.angle + d_ang))
    d = int(diag * size * sin(plane.angle - d_ang))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('thrusting')
                plane.thrust_up(5)
            if event.key == pygame.K_s:
                plane.thrust_up(-5)
            if event.key == pygame.K_d:
                plane.rotate(-0.04)
            if event.key == pygame.K_a:
                plane.rotate(0.04)
            


    '''
    pygame.draw.polygon(screen, (255, 255, 50), 
            ((CENTER[0] + a+ dx, CENTER[1] -b- dy), (CENTER[0] + c+ dx, CENTER[1] -d- dy),
             (CENTER[0] - a+ dx, CENTER[1] +b- dy), (CENTER[0] - c+ dx, CENTER[1] +d- dy))
            )
            '''
    pygame.draw.polygon(screen, (255, 255, 50), 
            ((CENTER[0] + a, CENTER[1] -b- dy), (CENTER[0] + c, CENTER[1] -d- dy),
             (CENTER[0] - a, CENTER[1] +b- dy), (CENTER[0] - c, CENTER[1] +d- dy))
            )

    pygame.draw.rect(screen, (100, 100, 100), (0, SCREEN_SIZE[1]-300, 20, 300))
    pygame.draw.rect(screen, (240, 100, 100), (0, SCREEN_SIZE[1]-int(3*plane.thrust), 20, int(3*plane.thrust)))
    pygame.display.update()
    last_frame = time()


