import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 800))




#фон
line(screen, (50, 255, 255), [200, 0], [200, 780], 800)
line(screen, (50, 255, 0), [200, 380], [200, 800], 800)

#солнце
l=1
while l<50:
    circle(screen, (50+l*4, 255, 255-5*l), (450, 125), 3*(50-l))
    l+=1


#лошадь
def loshad(angle, size, flip, x, y):
    """
    Функция рисует лошадь на экране.
    surface - объект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    size - масштаб изобажения в процентах
    flip - зеркальное отоброжение по вертикали( 1-изображение отображенно, 0-изображение не отображено)
    x,y - координаты левого верхнего угла изображения
    """
    surface = pygame.Surface((600, 800), pygame.SRCALPHA)
    #хвост
    ellipse(surface, (220, 220, 255), [50+x, 300+y, 55, 20])
    ellipse(surface, (255, 200, 255), [40+x, 290+y, 55, 20])
    ellipse(surface, (255, 255, 200), [30+x, 310+y, 49, 10])
    ellipse(surface, (220, 220, 255), [50+x, 320+y, 55, 20])
    ellipse(surface, (255, 220, 255), [57+x, 315+y, 55, 20])
    ellipse(surface, (255, 255, 200), [55+x, 275+y, 49, 10])
    ellipse(surface, (255, 220, 200), [70+x, 310+y, 55, 20])
    ellipse(surface, (255, 220, 200), [35+x, 275+y, 55, 20])
    ellipse(surface, (220, 200, 255), [25+x, 280+y, 49, 10])
    ellipse(surface, (255, 255, 220), [30+x, 320+y, 55, 15])
    ellipse(surface, (220, 200, 255), [65+x, 290+y, 49, 16])
    circle(surface, (200, 200, 100), [80+x, 240+y], 30)
    ellipse(surface, (220, 200, 255), [75+x, 245+y, 50, 30]) #
    ellipse(surface, (220, 255, 255), [35+x, 255+y, 50, 30])
    ellipse(surface, (255, 200, 255), [25+x, 245+y, 55, 20])
    ellipse(surface, (255, 200, 200), [40+x, 225+y, 55, 30])
    #туловище
    ellipse(surface, (255, 255, 255), [80+x, 180+y, 200, 100])
    line(surface, (255, 255, 255), [100+x, 225+y], [100+x, 345+y], 20)
    line(surface, (255, 255, 255), [135+x, 225+y], [135+x, 330+y], 15)
    line(surface, (255, 255, 255), [225+x, 100+y], [225+x, 225+y], 60)
    line(surface, (255, 255, 255), [205+x, 225+y], [205+x, 345+y], 20)
    line(surface, (255, 255, 255), [240+x, 225+y], [240+x, 330+y], 15)
    #голова
    ellipse(surface, (255, 255, 255), [200+x, 90+y, 80, 50])
    ellipse(surface, (255, 255, 255), [220+x, 105+y, 90, 35])
    #грива
    ellipse(surface, (220, 220, 255), [170+x, 110+y, 55, 20])
    ellipse(surface, (255, 200, 255), [160+x, 125+y, 55, 20])
    ellipse(surface, (255, 255, 200), [170+x, 145+y, 49, 10])
    ellipse(surface, (220, 220, 255), [165+x, 165+y, 55, 20])
    ellipse(surface, (255, 220, 255), [175+x, 155+y, 55, 20])
    ellipse(surface, (255, 255, 200), [180+x, 170+y, 49, 10])
    ellipse(surface, (220, 200, 255), [170+x, 120+y, 55, 20])
    ellipse(surface, (255, 200, 255), [160+x, 135+y, 55, 20])
    ellipse(surface, (255, 255, 200), [170+x, 149+y, 49, 10])
    ellipse(surface, (220, 200, 255), [165+x, 179+y, 55, 20])
    ellipse(surface, (255, 220, 255), [175+x, 135+y, 55, 20])
    ellipse(surface, (255, 255, 200), [180+x, 167+y, 49, 10])
    ellipse(surface, (255, 200, 220), [150+x, 120+y, 60, 25])
    ellipse(surface, (255, 200, 255), [130+x, 135+y, 55, 20])
    ellipse(surface, (200, 200, 255), [140+x, 149+y, 59, 15])
    ellipse(surface, (220, 230, 255), [145+x, 179+y, 60, 20])
    ellipse(surface, (220, 230, 200), [125+x, 152+y, 60, 20])
    ellipse(surface, (230, 250, 200), [135+x, 172+y, 50, 20])
    ellipse(surface, (250, 240, 200), [120+x, 167+y, 65, 20])
    ellipse(surface, (225, 200, 190), [200+x, 80+y, 45, 20])
    ellipse(surface, (245, 220, 200), [185+x, 90+y, 35, 25])
    polygon(surface, (225, 200, 190), [[230+x, 90+y], [260+x, 95+y], [250+x, 10+y]])
    ellipse(surface, (205, 50, 255), [238+x, 100+y, 20, 17])
    ellipse(surface, (0, 0, 0), [245+x, 105+y, 8, 8])
    ellipse(surface, (0, 0, 0), [245+x, 105+y, 8, 8])
    ellipse(surface, (255, 255, 255), [242+x, 103+y, 10, 4])
    surface = pygame.transform.rotozoom(surface, angle, size/100)
    if flip==1:
        surface = pygame.transform.flip(surface, 1, 0)

    rect = surface.get_rect()
    screen.blit(surface, rect)


#фон
def fon():
    line(screen, (245, 220, 255), [180, 350], [180, 480], 25)
    ellipse(screen, (0, 130, 0), [100, 40, 160, 160])
    ellipse(screen, (50, 255, 0), [100, 40, 160, 160], 5)
    ellipse(screen, (220, 180, 180), [180, 70, 60, 40])
    ellipse(screen, (50, 255, 0), [180, 70, 60, 40], 5)
    ellipse(screen, (0, 130, 0), [30, 120, 300, 160])
    ellipse(screen, (50, 255, 0), [30, 120, 300, 160], 5)
    ellipse(screen, (220, 180, 180), [230, 200, 60, 40])
    ellipse(screen, (50, 255, 0), [230, 200, 60, 40], 5)
    ellipse(screen, (220, 180, 180), [90, 170, 60, 40])
    ellipse(screen, (50, 255, 0), [90, 170, 60, 40], 5)
    ellipse(screen, (0, 130, 0), [0, 100, 120, 300])
    ellipse(screen, (0, 255, 0), [0, 100, 120, 300], 5)
    ellipse(screen, (220, 180, 180), [60, 155, 30, 60])
    ellipse(screen, (50, 255, 0), [60, 155, 30, 60], 5)
    ellipse(screen, (0, 130, 0), [90, 230, 180, 120])
    ellipse(screen, (0, 255, 0), [90, 230, 180, 120], 5)
    ellipse(screen, (0, 130, 0), [0, 300, 170, 150])
    ellipse(screen, (0, 255, 0), [0, 300, 170, 150], 5)
    ellipse(screen, (220, 180, 180), [100, 370, 30, 50])
    ellipse(screen, (50, 255, 0), [100, 370, 30, 50], 5)
    ellipse(screen, (0, 130, 0), [140, 300, 120, 90])
    ellipse(screen, (0, 255, 0), [140, 300, 120, 90], 5)
    line(screen, (245, 220, 255), [65, 470], [65, 580], 25)
    ellipse(screen, (0, 130, 0), [0, 350, 120, 180])
    ellipse(screen, (0, 255, 0), [0, 350, 120, 180], 5)
    ellipse(screen, (220, 180, 180), [190, 330, 50, 30])
    ellipse(screen, (50, 255, 0), [190, 330, 50, 30], 5)
    ellipse(screen, (0, 130, 0), [110, 360, 180, 100])
    ellipse(screen, (0, 255, 0), [110, 360, 180, 100], 5)
    ellipse(screen, (220, 180, 180), [230, 395, 30, 30])
    ellipse(screen, (50, 255, 0), [230, 395, 30, 30], 5)
    line(screen, (245, 220, 255), [200, 500], [200, 600], 25)
    ellipse(screen, (0, 130, 0), [120, 430, 160, 120])
    ellipse(screen, (0, 255, 0), [120, 430, 160, 120], 5)
    ellipse(screen, (220, 180, 180), [210, 490, 50, 25])
    ellipse(screen, (50, 255, 0), [210, 490, 50, 25], 5)
    ellipse(screen, (220, 180, 180), [20, 415, 30, 20])
    ellipse(screen, (50, 255, 0), [20, 415, 30, 20], 5)
    line(screen, (245, 220, 255), [110, 650], [110, 780], 25)
    ellipse(screen, (0, 130, 0), [60, 500, 100, 100])
    ellipse(screen, (0, 255, 0), [60, 500, 100, 100], 5)
    ellipse(screen, (0, 130, 0), [30, 570, 150, 100])
    ellipse(screen, (0, 255, 0), [30, 570, 150, 100], 5)
    ellipse(screen, (0, 130, 0), [40, 640, 130, 90])
    ellipse(screen, (0, 255, 0), [40, 640, 130, 90], 5)
    ellipse(screen, (220, 180, 180), [130, 610, 40, 30])
    ellipse(screen, (50, 255, 0), [130, 610, 40, 30], 5)
    ellipse(screen, (220, 180, 180), [110, 520, 30, 34])
    ellipse(screen, (50, 255, 0), [110, 520, 30, 34], 5)
    ellipse(screen, (220, 180, 180), [120, 700, 25, 25])
    ellipse(screen, (50, 255, 0), [120, 700, 25, 25], 5)
fon()



#loshad(0, 100, 0, 100, 400)
loshad(0, 30, 0, 10, 10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
