from turtle import circle
import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))
kol = 0  #начальное количество очков

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
i = 1
j = 1
k = 1
p = 1

def new_figura():
    '''рисует  '''
    global x, y, r, color, z
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    z = randint(1,2)
    if z == 1:
        circle(screen, color, (x, y), r)
    else:
        rect(screen, color, (x-r, y-r, 2*r, 2*r))

new_figura()
x1 = x
y1 = y
r1 = r
color1 = color
z1 = z

new_figura()
x2 = x
y2 = y
r2 = r
color2 = color
z2 = z

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xl=event.pos[0]
            yl=event.pos[1]
            if math.sqrt((x1-xl)**2+(y1-yl)**2) <= r1 and z1 == 1: #сравнивает расстояние от центра шарика до нажатия мышкой с радиусом шарика
                kol=kol+1
                pygame.display.update()
                new_figura()
                x1 = x
                y1 = y
                r1 = r
                color1 = color
                z1 = z
                l = randint(1, 2)
                if l == 1:
                    i = -1 + 0
                else:
                    i = -1 + 2
                o = randint(1, 2)
                if o == 1:
                    y = -1 + 0
                else:
                    y = -1 + 2

            elif xl <= x1 + r1 and xl >= x1-r1 and yl <= y1 + r1 and yl >= y1 - r1 and z1 == 2:
                kol=kol+1
                pygame.display.update()
                new_figura()
                x1 = x
                y1 = y
                r1 = r
                color1 = color
                z1 = z
                l = randint(1, 2)
                if l == 1:
                    i = -1 + 0
                else:
                    i = -1 + 2
                o = randint(1, 2)
                if o == 1:
                    y = -1 + 0
                else:
                    y = -1 + 2

            if math.sqrt((x2-xl)**2+(y2-yl)**2) <= r2 and z2 == 1: #сравнивает расстояние от центра шарика до нажатия мышкой с радиусом шарика
                kol=kol+1
                pygame.display.update()
                new_figura()
                x2 = x
                y2 = y
                r2 = r
                color2 = color
                z2 = z
                l = randint(1, 2)
                if l == 1:
                    k = -1 + 0
                else:
                    k = -1 + 2
                o = randint(1, 2)
                if o == 1:
                    p = -1 + 0
                else:
                    p = -1 + 2

            elif xl <= x2 + r2 and xl >= x2-r2 and yl <= y2 + r2 and yl >= y2 - r2 and z2 == 2:
                kol=kol+1
                pygame.display.update()
                new_figura()
                x2 = x
                y2 = y
                r2 = r
                color2 = color
                z2 = z
                l = randint(1, 2)
                if l == 1:
                    k = -1 + 0
                else:
                    k = -1 + 2
                o = randint(1, 2)
                if o == 1:
                    p = -1 + 0
                else:
                    p = -1 + 2


    if z1 == 1:
        circle(screen, color1, (x1, y1), r1)
    elif z1 == 2:
        rect(screen, color1, (x1 - r1, y1 - r1, 2 * r1, 2 * r1))

    if z2 == 1:
        circle(screen, color2, (x2, y2), r2)
    elif z2 == 2:
        rect(screen, color2, (x2 - r2, y2 - r2, 2 * r2, 2 * r2))

    pygame.display.update()


    if x1 < 1200 - r1 and x1 > r1:
        x1=x1+i
    elif x1 == 1200 - r1 or x1 == r1:
        i=-i
        x1=x1+i

    if y1 < 900 - r1 and y1 > r1:
        y1=y1+j
    elif y1 == 900 - r1 or y1 == r1:
        j=-j
        y1=y1+j

    if x2 < 1200 - r2 and x2 > r2:
        x2 = x2 + k
    elif x2 == 1200 - r2 or x2 == r2:
        k = -k
        x2 = x2 + k

    if y2 < 900 - r2 and y2 > r2:
        y2 = y2 + p
    elif y2 == 900 - r2 or y2 == r2:
        p = -p
        y2 = y2 + p

    print(kol) #выводит текущее кол-во очков в консоль
    screen.fill(BLACK) #очистка экрана

pygame.quit()