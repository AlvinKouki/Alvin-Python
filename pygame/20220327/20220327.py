from asyncio import events
from turtle import circle, update
import pygame

import pygame
import sys
import random


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
bg_img = "20220327/Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()

gophers = pygame.image.load("20220327/Gophers150.png")

Blue = (0, 0, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
screen = pygame.display.set_mode([bg_x, bg_y])  #設定視窗
pygame.display.set_caption("打地鼠")

sur = pygame.Surface([bg_x, bg_y])  #設定背景容器

pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]

#score
score = 0  #score count
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

tick = 0
max_tick = 20
pos = pos6[0]  #外面設定圓的位置

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1

    #每偵循環執行的代碼
    if tick > max_tick:
        new_pos = random.randint(0, 5)  #隨機0到5
        pos = pos6[new_pos]  #更新外部紀錄的圓的位置
        tick = 0

    else:
        tick += 1  #增加計數器

    #刷新畫面
    sur.blit(bg, (0, 0))
    sur.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))
    #隨機位置
    screen.blit(sur, (0, 0))

    score_sur = score_font.render(str(score), False, Red)  #!!生成計數表面
    screen.blit(score_sur, (10, 10))
    pygame.display.update()
