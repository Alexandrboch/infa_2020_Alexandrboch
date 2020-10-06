from turtle import circle
import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
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

def new_ball():  #рисует шарик произвольного радиуса(от 10 до 100) в произвольном месте экрана
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click():  #выводит координаты и рдиус произвольного шарика в консоль
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1=event.pos[0]
            y1=event.pos[1]
            if math.sqrt((x-x1)**2+(y-y1)**2) <= r: #сравнивает расстояние от центра шарика до нажатия мышкой с радиусом шарика
                kol=kol+1

    new_ball()
    click()
    pygame.display.update()
    print(kol) #выводит текущее кол-во очков в консоль
    screen.fill(BLACK) #очистка экрана

pygame.quit()

