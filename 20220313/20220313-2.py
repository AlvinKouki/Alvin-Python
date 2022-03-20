import imp
import random
from re import X
from tkinter import font
import pygame
import sys
import math


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bg = pygame.image.load('20220313/snow.jpg')
bg_x = bg.get_width()
bg_y = bg.get_height()

screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption('My Game')

mp3_path = "20220320/snow-dream.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(6000000)

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, BLACK)
title_w = title.get_width()
title_h = title.get_height()

picture = False
clock = pygame.time.Clock()
x_site = random.randrange(0, bg_x)
y_site = random.randrange(-10, -1)
x_shift = random.randrange(-1, 1)
radius = random.randint(4, 6)
picture = False
cnt = 0
while 1:
    if cnt <= 1:
        cnt += 1
    else:
        cnt = 0
    clock.tick(50)
    x_shift = random.randrange(-10, 10)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, title_w, title_h):
                picture = not (picture)

    screen.blit(bg, (0, 0))

    if picture:
        title = font.render('Stop', True, BLACK)
    else:
        title = font.render('Start', True, BLACK)
        pygame.draw.circle(screen, WHITE, (x_site, y_site), radius)
        x_site += x_shift
        y_site += radius

        if y_site > bg_y or x_site > bg_x:
            y_site = random.randrange(-10, -1)
            x_site = random.randrange(0, bg_x)
    screen.blit(title, (0, 0))

    pygame.display.update()