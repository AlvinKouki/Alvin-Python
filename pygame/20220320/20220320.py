import random
from tkinter import font
import pygame
import sys
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()

bg = pygame.image.load('20220313/snow.jpg')
bg_x = bg.get_width()
bg_y = bg.get_height()

screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption('My Game')

mp3_path = "20220320\music2.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(6000000)

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, BLACK)
title_w = title.get_width()
title_h = title.get_height()
picture = False

title2 = font.render('fast', True, BLACK)
title2_w = title2.get_width()
title2_h = title2.get_height()
speed = True  # T=Fast, F=Slow

clock = pygame.time.Clock()

snow_list = []
for i in range(100):
    x_site = random.randrange(0, bg_x)
    y_site = random.randrange(-100, -1)
    x_shift = random.randrange(-1, 1)
    radius = random.randint(4, 6)
    snow_list.append([x_site, y_site, x_shift, radius])

cnt = 0
while True:
    if speed:
        title2 = font.render('fast', True, BLACK)
        clock.tick(200)
    else:
        title2 = font.render('slow', True, BLACK)
        clock.tick(20)

    if cnt <= 1:
        cnt += 1
        pygame.mixer.music.pause()
    else:
        cnt = 0
        pygame.mixer.music.pause()

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, title_w, title_h):
                picture = not (picture)
            if check_click(mouse_pos, 100, 100, title2_w + 100,
                           title2_h + 100):
                speed = not (speed)

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    screen.blit(title2, (100, 100))

    if picture:
        title = font.render('Stop', True, BLACK)
    else:
        title = font.render('Start', True, BLACK)

        for snow in snow_list:
            pygame.draw.circle(screen, WHITE, (snow[0], snow[1]), snow[3])
            snow[0] += snow[2]
            snow[1] += snow[3]

            if snow[1] > bg_y or snow[0] > bg_x:
                snow[1] = random.randrange(-100, -1)
                snow[0] = random.randrange(0, bg_x)

    pygame.display.update()