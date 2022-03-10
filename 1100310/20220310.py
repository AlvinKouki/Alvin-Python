import pygame
import sys
import math

pygame.init()
width = 1000
height = 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')
bg = pygame.Surface(screen.get_size())
# bg.fill((83, 197, 192))
# pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
# pygame.draw.rect(bg, (0, 0, 255), [100, 100, 100, 100], 0)
# pygame.draw.ellipse(bg, (0, 0, 255), [100, 100, 200, 500], 0)
# pygame.draw.polygon(bg, (255, 0, 0), [[200, 300], [100, 100], [50, 350]], 0)
# pygame.draw.arc(bg, (10, 255, 255), [100, 100, 200, 50], math.radians(270),
#                 math.radians(0), 2)
# pygame.draw.line(bg, (0, 255, 255), (300, 200), (100, 100), 1)



# pygame.draw.ellipse(bg,(0,0,0),[250,250,340,340],0)
# pygame.draw.circle(bg, (255, 0, 0), (500, 400), 30, 0)
# pygame.draw.circle(bg, (255, 0, 0), (350, 400), 30, 0)
# pygame.draw.arc(bg, (80, 80, 80), [350, 400, 150, 110], math.radians(180),math.radians(0), 2)

picture=False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            picture = not(picture)

    if picture:
        pygame.draw.ellipse(bg,(0,0,0),[250,250,340,340],0)
        pygame.draw.circle(bg, (255, 0, 0), (500, 400), 30, 0)
        pygame.draw.circle(bg, (255, 0, 0), (350, 400), 30, 0)
        pygame.draw.arc(bg, (80, 80, 80), [350, 400, 150, 110], math.radians(180),math.radians(0), 2)
    else:
        bg.fill((83, 197, 192))

    screen.blit(bg, (0, 0))
    pygame.display.update()