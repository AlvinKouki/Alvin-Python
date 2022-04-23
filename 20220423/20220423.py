#===載入套件開始
from pickle import TRUE
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***

#===初始化設定開始===
clock = pygame.time.Clock()
LIMIT_LOW = 140
LIMIT_HIGH = 140
pygame.init()
pygame.init()
timer = 0
Red = (255, 0, 0)
#***初始化設定結束***

#===載入圖片開始===
img = pygame.image.load("bg.png")
img_dinosaur = [pygame.image.load("小恐龍1.png"), pygame.image.load("小恐龍2.png")]
img_cacti = pygame.image.load("cacti.png")

#***載入圖片結束***

#===遊戲視窗設定開始===

bg_x = img.get_width()
bg_y = img.get_height()
bg_size = (bg_x, bg_y)
roll_x = 0
#***遊戲視窗設定結束***
pygame.display.set_caption("Dinosaur")
screen = pygame.display.set_mode(bg_size)
#===分數設定開始=== 
score=0
got_score=False
typeface=pygame.font.get_default_font()
score_font-pygame.font.Font(typeface,36)
score_sur=score_font.render(str(score), False,Red)

def get_score(win):
    global score, score_sur, got_score

    if (get_score==True):



#***分數設定結束***

#===恐龍設定開始===
def move_dinosaur(win,timer):

#***恐龍設定結束***
ds_x = 50
ds_y = LIMIT_LOW
jumpstate = False
jumpvalue = 0



def move_dinosaur(win, timer):
    global ds_x, ds_y, jumpstate, jumpvalue
    if jumpstate:
        if ds_y >= LIMIT_LOW:
            jumpvalue = -10
        if ds_y <= 0:
            jumpvalue = 10
        ds_y += jumpvalue
        if ds_y == LIMIT_LOW:
            jumpstate = False
    win.blit(img_dinosaur[timer % len(img_dinosaur)], [ds_x, ds_y])


#===仙人掌設定開始===
cacti_x = bg_x - 100
cacti_y = LIMIT_LOW
cacti_shift = 10
def move_cacti(win):
    global cacti_x, cacti_y,cacti_shift 
    global score,score_sur, got_score
    cacti_x-=cacti_shift
    if (cacti_x<0):
        got_score=True
        cacti_shift=10
    win.blit(img_cacti, [cacti_x,cacti_y])
    cacti_dist=int((cacti_w+cacti_h)/2)

#***仙人掌設定結束***



def move_cacti(win):
    global cacti_x, cacti_y, cacti_shift
    win.blit(img_cacti, [cacti_x, cacti_y])
    cacti_x = (cacti_x - cacti_shift) % bg_x


#***碰撞設定結束***
def is_hit(x1,y1,x2,y2,r):
    if ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<(r*r)):
        return True
    else:
        return False

#***碰撞設定結束***

#===GameOver設定開始===

#***GameOver設定結束***

#===主程式開始===
while 1:
    clock.tick(20)
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:
                jumpstate = True
    #===計時與速度===

    #===偵測鍵盤事件開始===

    #===遊戲結束===
    roll_x = (roll_x - 10) % bg_x
    print(roll_x)
    screen.blit(img, [roll_x - bg_x, 0])
    screen.blit(img, [roll_x, 0])
    #===遊戲進行===

    #===更新角色狀態===
    
    move_dinosaur(screen, timer)
    move_cacti(screen)
    get_score(screen)
    if (is_hit(ds_x,ds_y,cacti_x,cacti_y,cacti_dist)):
        print("hit")   
pygame.display.update()
#===主程式結束===
