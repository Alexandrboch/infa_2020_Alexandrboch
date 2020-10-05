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
    h = {
        0: [220, 220, 255, 50, 300, 55, 20],
        1: [255, 200, 255, 40, 290, 55, 20],
        2: [255, 255, 200, 30, 310, 49, 10],
        3: [220, 220, 255, 50, 320, 55, 20],
        4: [255, 220, 255, 57, 315, 55, 20],
        5: [255, 255, 200, 55, 275, 49, 10],
        6: [255, 220, 200, 70, 310, 55, 20],
        7: [255, 220, 200, 35, 275, 55, 20],
        8: [220, 200, 255, 25, 280, 49, 10],
        9: [255, 255, 220, 30, 320, 55, 15],
        10: [220, 200, 255, 65, 290, 49, 16],
        11: [220, 200, 255, 75, 245, 50, 30],
        12: [220, 255, 255, 35, 255, 50, 30],
        13: [255, 200, 255, 25, 245, 55, 20],
        14: [255, 200, 200, 40, 225, 55, 30]
    }
    for x in range(15):
        ellipse(surface, (h[x][0], h[x][1], h[x][2]), [h[x][3] + x, h[x][4] + y, h[x][5], h[x][6]])
    circle(surface, (200, 200, 100), [80 + x, 240 + y], 30)


    #туловище
    t = {
        0: [255, 255, 255, 100, 225, 100, 345, 20],
        1: [255, 255, 255, 135, 225, 135, 330, 15],
        2: [255, 255, 255, 225, 100, 225, 225, 60],
        3: [255, 255, 255, 205, 225, 205, 345, 20],
        4: [255, 255, 255, 240, 225, 240, 330, 15]
    }
    for x in range(5):
        line(surface, (t[x][0], t[x][1], t[x][2]), [t[x][3] + x, t[x][4] + y], [t[x][5] + x, t[x][6] + y], t[x][7])
    ellipse(surface, (255, 255, 255), [80 + x, 180 + y, 200, 100])


    #голова
    ellipse(surface, (255, 255, 255), [200+x, 90+y, 80, 50])
    ellipse(surface, (255, 255, 255), [220+x, 105+y, 90, 35])


    #грива
    g = {
    0: [220, 220, 255, 170, 110, 55, 20],
    1: [255, 200, 255, 160, 125, 55, 20],
    2: [255, 255, 200, 170, 145, 49, 10],
    3: [255, 220, 255, 175, 155, 55, 20],
    4: [255, 255, 200, 180, 170, 49, 10],
    5: [220, 200, 255, 170, 120, 55, 20],
    6: [255, 200, 255, 160, 135, 55, 20],
    7: [255, 255, 200, 170, 149, 49, 10],
    8: [220, 200, 255, 165, 179, 55, 20],
    9: [255, 220, 255, 175, 135, 55, 20],
    10: [255, 255, 200, 180, 167, 49, 10],
    11: [255, 200, 220, 150, 120, 60, 25],
    12: [255, 200, 255, 130, 135, 55, 20],
    13: [200, 200, 255, 140, 149, 59, 15],
    14: [220, 230, 200, 125, 152, 60, 20],
    15: [230, 250, 200, 135, 172, 50, 20],
    16: [250, 240, 200, 120, 167, 65, 20],
    17: [225, 200, 190, 200, 80, 45, 20],
    18: [245, 220, 200, 185, 90, 35, 25]
    }
    for x in range(19):
        ellipse(surface, (g[x][0], g[x][1], g[x][2]), [g[x][3], g[x][4], g[x][5], g[x][6]])
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