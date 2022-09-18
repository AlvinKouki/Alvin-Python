from asyncio import events
import imp
from turtle import circle, update
import pygame
import os
import time
import pygame
import sys
import random

os.chdir(sys.path[0])
from pygame.locals import *


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
gophers = pygame.image.load("Gophers150.png")
gophers2 = pygame.image.load("Gophers2_150.png")
pygame.mixer.music.load("hit.mp3")
times = 0
times_max = 20
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()

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

end_font = pygame.font.Font(typeface, 36)
end_sur = end_font.render(str(times), True, Red)

tick = 0
max_tick = 20
pos = pos6[0]  #外面設定圓的位置

times = 0
times_max = 100

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
mpos = (0, 0)
while True:
    clock.tick(30)
    hammer = ham2
    hit = gophers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1
                    score += 1
                    hit = gophers2
                    pygame.mixer.music.play()
        elif event.type == pygame.MOUSEMOTION:
            mpos = pygame.mouse.get_pos()

    if times > times_max:
        sur.fill((0, 0, 0))
        pygame.mouse.set_visible(True)
        end_sur = score_font.render(
            "Your score is:{}/{}".format(score, times_max), False, Red)
        screen.blit(sur, (0, 0))
        screen.blit(end_sur, (100, 100))
        pygame.display.flip()
    else:
        #每偵循環執行的代碼
        if tick > max_tick:
            new_pos = random.randint(0, 5)  #隨機0到5
            pos = pos6[new_pos]  #更新外部紀錄的圓的位置
            tick = 0
            times += 1
        else:
            tick += 1  #增加計數器

        #刷新畫面
        sur.blit(bg, (0, 0))
        sur.blit(hit,
                 (pos[0] - hit.get_width() / 2, pos[1] - hit.get_height() / 2))
        #隨機位置
        # pygame.draw.circle(sur, Blue, mpos, 10)
        sur.blit(hammer, (mpos[0] - hammer.get_width() / 2,
                          mpos[1] - hammer.get_height() / 2))
        screen.blit(sur, (0, 0))

        score_sur = score_font.render(str(score), False, Red)  #!!生成計數表面
        screen.blit(score_sur, (10, 10))
        pygame.display.update()
        if hammer == ham1 or hit == gophers2:
            time.sleep(0.1)